import pandas as pd
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time

def run_scraper():
    print("🚀 Starting Professional Scraper...")
    
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Target URL
        url = "https://nigeriapropertycentre.com/for-rent/kaduna"
        print(f"📡 Accessing: {url}")
        
        try:
            page.goto(url, timeout=60000)
            # Give it time to load dynamic content
            page.wait_for_timeout(5000) 
            
            html = page.content()
            soup = BeautifulSoup(html, 'html.parser')
            
            # Find the property containers
            listings = soup.find_all("div", class_="wp-block-body")
            
            data = []
            for item in listings:
                # Scrape Title
                title_tag = item.find("h4", class_="content-title")
                title = title_tag.get_text(strip=True) if title_tag else "N/A"
                
                # Scrape Price
                price_tag = item.find("span", class_="pull-sm-left")
                price = price_tag.get_text(strip=True) if price_tag else "N/A"
                
                # Scrape Address
                address_tag = item.find("address")
                address = address_tag.get_text(strip=True) if address_tag else "N/A"
                
                data.append({
                    "Title": title, 
                    "Price": price, 
                    "Address": address
                })
            
            # Convert to DataFrame and save
            if data:
                df = pd.DataFrame(data)
                df.to_csv("kaduna_properties.csv", index=False)
                print(f"✅ Success! Saved {len(df)} properties to 'kaduna_properties.csv'")
            else:
                print("⚠️ No data found. The website structure might have changed.")
                
        except Exception as e:
            print(f"❌ Error occurred: {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    run_scraper()