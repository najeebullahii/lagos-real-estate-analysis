# Lagos Real Estate Market Analysis

**Live Dashboard**: [View on Tableau Public](https://public.tableau.com/app/profile/najib.njidda/viz/LAGOSREALESTATEMARKETANALYSIS/Dashboard1?publish=yes)

---

## What This Project Is About

I built an interactive dashboard that analyzes 1,993 properties across Lagos to help investors, buyers, and renters make smarter real estate decisions. I scraped property listings from Nigeria Property Centre, cleaned the messy data, and created visualizations that reveal some pretty interesting investment patterns.

The main finding? Investment returns vary wildly across Lagos - from 9.3% yields in Ibeju Lekki to 0.3% in Ikorodu. That's a 30x difference in the same city.

---

## Why I Built This

I got interested in this project because Lagos real estate data is all over the place. If you want to know whether ₦500M is a fair price for a property in Lekki, or what the typical rent is for a 3-bedroom in Ikoyi, there's no easy way to find out. Everyone just relies on what their agent tells them or what they've heard from friends.

I wanted to see if I could gather actual data and find patterns that would be useful for real decisions. Plus, I wanted to challenge myself with an end-to-end project - from web scraping to data cleaning to building something interactive.

---

## The Business Questions

Here's what I tried to answer:

**Investment questions:**
- Which areas give you the best rental ROI?
- Where should you definitely not invest?
- What's the overall state of the market?

**Buyer questions:**
- Is the price I'm seeing reasonable for this area?
- What's the typical price range for 4-bedroom properties in Lekki?

**Renter questions:**
- Am I getting a fair deal on rent?
- What should I expect to pay for a 3-bedroom in different areas?

---

## What I Found

The data revealed some interesting patterns:

**Best investment areas** (based on rental yield):
1. Ibeju Lekki - 9.3% annual yield
2. Yaba - 9.1% annual yield  
3. Maryland - 5.2% annual yield

**Areas to avoid**:
1. Ikorodu - 0.3% yield (it would take 322 years of rent to pay back the purchase price!)
2. Surulere - 1.1% yield
3. Agege - 1.3% yield

**Market overview**:
- 1,993 properties analyzed (1,144 for sale, 687 for rent)
- Average sale price: ₦580M
- Average annual rent: ₦15M
- Lekki completely dominates with 47% of all listings

**Surprising insight**: Ikoyi has the highest average sale price (₦1.66B) but one of the worst yields (2.2%). Expensive doesn't mean profitable.

---

## How I Built This

### Data Collection

I scraped 2,138 property listings from Nigeria Property Centre using Python (Playwright and BeautifulSoup). The scraper pulled titles, prices, and addresses for properties across Lagos.

### Data Cleaning

The raw data was messy, prices in different currencies, inconsistent formatting, clear outliers. I ended up doing 3 separate cleaning rounds:

**Round 1 - Feature Engineering**
- Extracted bedroom counts and property types from listing titles using regex
- Broke down addresses into neighborhood, area, and state
- Standardized all prices to Naira
- Categorized each listing as Sale, Rent, or Short Let

**Round 2 - Outlier Removal**
- Removed obvious mislabeled data (like "sales" under ₦2M that were clearly rentals)
- Filtered out commercial properties and unrealistic bedroom counts
- Focused only on Lagos State

**Round 3 - Final Quality Control**
- Removed extreme rental outliers that would skew the analysis
- This made a huge difference, the maximum rent dropped from ₦1.5 billion to ₦50 million
- Average rent went from ₦23M to ₦15M (35% more accurate)
- Final dataset: 1,993 properties (removed 145 outliers total)

### Dashboard Creation

Built everything in Tableau with 11 different visualizations:
- KPI metrics showing market overview
- Bar charts comparing top areas by price
- Bedroom demand analysis
- Investment opportunity scatter plot
- Dual-axis chart showing both price-to-rent ratios and yields

I used LOD (Level of Detail) expressions to calculate area-level metrics like average prices and rental yields.

---

## Key Insights

**Geographic inequality is massive**. A 30x difference in investment returns within the same city tells you that location is everything. Property type and size matter far less than where you're buying.

**Premium areas aren't always profitable**. Ikoyi properties are expensive, but the rental yields are mediocre. You're paying for prestige, not cash flow.

**The market is concentrated**. Lekki has almost half of all listings. This could mean high demand, or it could mean the market is oversaturated. Would need sales velocity data to know for sure.

---

## Technical Details

**Tools used:**
- Web scraping: Python with Playwright and BeautifulSoup
- Data cleaning: Pandas
- Analysis & visualization: Tableau Desktop/Public
- Version control: Git and GitHub

**Python libraries:**
```
pandas==2.0.3
playwright==1.40.0
beautifulsoup4==4.12.2
```

---

## Running the Code

If you want to run this yourself:

1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Install Playwright browsers: `playwright install chromium`
4. Run the scraper: `python scripts/web_scraping.py` (optional - data is already included)
5. Clean the data: `python scripts/Lagos_data_cleaning.py`
6. Open the Tableau dashboard or view it on [Tableau Public](https://public.tableau.com/app/profile/najib.njidda/viz/LAGOSREALESTATEMARKETANALYSIS/Dashboard1?publish=yes)

---

---

## Limitations

A few things to keep in mind:

- This is a snapshot from one point in time, not a time series
- Only includes listed properties, not actual sales data
- Can't verify if listings are real or just aspirational pricing
- No information on how long properties stay on the market
- Missing context like neighborhood amenities, crime rates, schools, etc.

For a more complete analysis, I'd want to track listings over time and combine this with actual transaction data from the land registry.

---

---

## License

MIT License - feel free to use this code for your own projects.

---

## Acknowledgments

Data source: [Nigeria Property Centre](https://nigeriapropertycentre.com/)


---

*Last updated: February 2026*
