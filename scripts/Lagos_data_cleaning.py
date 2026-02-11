import pandas as pd
import re

# Load the raw data from CSV file
df = pd.read_csv(r"C:\Users\Najib\Documents\lagos_raw_data.csv")
df_clean = df.copy()

# Drop 'Details' if it exists and remove duplicates
if 'Details' in df_clean.columns:
    df_clean.drop(columns=['Details'], inplace=True)
df_clean = df_clean.drop_duplicates()

# Breaks down the address into more useful geographic levels

def extract_location(address):
    parts = [p.strip() for p in str(address).split(',')]
    state = parts[-1] if len(parts) >= 1 else "Unknown"
    area = parts[-2] if len(parts) >= 2 else state
    neighborhood = parts[-3] if len(parts) >= 3 else area
    return pd.Series([neighborhood, area, state])

df_clean[['Neighborhood', 'Main_Area', 'State']] = df_clean['Address'].apply(extract_location)

# Pulls out key information from the listing title
# Titles contain valuable structured data like "3 bedroom flat for rent"
def extract_features(title):
    title = str(title).lower()
    bed_match = re.search(r'(\d+)\s*bedroom', title)
    bedrooms = int(bed_match.group(1)) if bed_match else 0
    
    if 'duplex' in title: prop_type = 'Duplex'
    elif 'flat' in title or 'apartment' in title: prop_type = 'Flat'
    elif 'house' in title: prop_type = 'House'
    elif 'land' in title: prop_type = 'Land'
    elif 'office' in title: prop_type = 'Office Space'
    elif 'shop' in title: prop_type = 'Shop'
    else: prop_type = 'Other'
    return pd.Series([bedrooms, prop_type])

df_clean[['Bedrooms', 'Property_Type']] = df_clean['Title'].apply(extract_features)

# Cleaning up messy price data and figuring out whether each listing is for sale, rent, or short-term rental

def fix_price_and_category(row):
    price_str = str(row['Price']).lower()
    title_text = str(row['Title']).lower()
    
    # Extract Numeric Value (Handling Naira approximations for Dollar listings)
    if "approx. ₦" in price_str:
        naira_part = price_str.split("approx. ₦")[1]
        num_val = float(re.sub(r'[^\d]', '', naira_part))
    else:
        # Standard extraction (digits after the last currency symbol)
        digits = re.sub(r'[^\d]', '', price_str.split('₦')[-1])
        num_val = float(digits) if digits else 0.0
        
    # Determine Category based on Title and Price Keywords
    if 'short let' in title_text or 'per day' in price_str:
        category = 'Short Let'
    elif 'for rent' in title_text or 'per annum' in price_str or 'per month' in price_str:
        category = 'Rent'
    elif 'for sale' in title_text or 'joint venture' in title_text:
        category = 'Sale'
    else:
        # Fallback to current category if no keywords found
        category = row['Category'] if 'Category' in row else 'Other'
        
    return pd.Series([category, num_val])

df_clean[['Category', 'Price_Numeric']] = df_clean.apply(fix_price_and_category, axis=1)


# Filter for Lagos Only
df_clean = df_clean[df_clean['State'] == 'Lagos'].copy()

# Identify Outliers
# - Sales under 2M (usually mislabeled rent/placeholders)
# - Residential Rents over 100M (usually mislabeled sales)
is_low_sale = (df_clean['Category'] == 'Sale') & (df_clean['Price_Numeric'] < 2000000) & (~df_clean['Property_Type'].isin(['Land', 'Other']))
is_high_rent = (df_clean['Category'] == 'Rent') & (df_clean['Price_Numeric'] > 100000000) & (df_clean['Property_Type'].isin(['Flat', 'Duplex', 'House']))
is_junk = df_clean['Price_Numeric'] < 10000

df_clean = df_clean[~(is_low_sale | is_high_rent | is_junk)]
df_clean = df_clean[df_clean['Bedrooms'] <= 20].copy()
