# 🏠 Lagos Real Estate Market Analysis

[![Tableau](https://img.shields.io/badge/Tableau-Public-blue)](https://public.tableau.com/app/profile/najib.njidda/viz/LAGOSREALESTATEMARKETANALYSIS/Dashboard1?publish=yes)
[![Python](https://img.shields.io/badge/Python-3.8+-green)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Interactive Dashboard**: [View on Tableau Public →](https://public.tableau.com/app/profile/najib.njidda/viz/LAGOSREALESTATEMARKETANALYSIS/Dashboard1?publish=yes)

---

## 📋 Table of Contents
- [Problem Statement](#-problem-statement)
- [Why This Project?](#-why-this-project)
- [Business Questions Answered](#-business-questions-answered)
- [Approach](#-approach)
- [Key Results](#-key-results)
- [Visual Outputs](#-visual-outputs)
- [Technical Stack](#-technical-stack)
- [How to Run](#-how-to-run)
- [Project Structure](#-project-structure)
- [Key Insights](#-key-insights)
- [Conclusion](#-conclusion)
- [Connect With Me](#-connect-with-me)

---

## 🎯 Problem Statement

The Lagos real estate market lacks **transparent, data-driven intelligence** for investment decisions. Key challenges include:

- **Investors** struggle to calculate realistic rental ROI across different areas
- **Home buyers** can't easily benchmark fair market values
- **Renters** have no data to identify reasonable rental rates
- **Real estate agents** lack quantitative tools to advise clients

**The core problem**: Without centralized data and analytics, stakeholders make decisions based on anecdotal information rather than market evidence.

---

## 💡 Why This Project?

As someone passionate about using **data analytics to solve real-world problems**, I chose this project to:

1. **Address a Real Gap**: Lagos real estate data is fragmented across multiple platforms
2. **Demonstrate End-to-End Skills**: From web scraping to data cleaning to interactive visualization
3. **Create Business Value**: Deliver actionable investment intelligence, not just pretty charts
4. **Showcase Data Quality Standards**: Performed 3 rounds of cleaning, improving accuracy by 35%

This project demonstrates my ability to **take messy real-world data and transform it into business intelligence**.

---

## 🔍 Business Questions Answered

### Primary Questions:
1. **Which areas offer the best rental investment ROI?**
   - Answer: Ibeju Lekki (9.3% yield), Yaba (9.1% yield), Maryland (5.2% yield)

2. **Is ₦500M a fair price for a 4-bedroom duplex in Lekki?**
   - Answer: Yes – average sale price in Lekki is ₦485M

3. **What's a typical annual rent for a 3-bedroom flat in Ikoyi?**
   - Answer: ₦37M per year

4. **Which areas should investors avoid?**
   - Answer: Ikorodu (0.3% yield = 322 years to break even!), Surulere (1.1% yield)

5. **What property types and bedroom counts are most in demand?**
   - Answer: 4-bedroom properties dominate (26% of market), split evenly between duplexes (40%) and flats (40%)

### Strategic Insights:
- **30x variation in ROI** across Lagos areas (9.3% vs 0.3%)
- **Lekki dominates** with 47% market share (936 properties)
- **Overall market**: 39x price-to-rent ratio, 2.6% average yield

---

## 🛠️ Approach

### 1. Data Collection (Web Scraping)
- **Source**: [Nigeria Property Centre](https://nigeriapropertycentre.com/)
- **Method**: Python with Playwright + BeautifulSoup
- **Coverage**: 2,138 property listings across Lagos
- **Data Points**: Title, Price, Address, Category

```python
# Key scraping technology
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
```

### 2. Data Cleaning (3-Round Process)

**Round 1: Feature Engineering**
- Extracted bedrooms, property type from titles using regex
- Parsed addresses into Neighborhood, Main Area, State
- Standardized price formats (handled Naira/Dollar conversions)
- Categorized listings: Sale, Rent, Short Let

**Round 2: Outlier Removal**
- Removed sales <₦2M (mislabeled rentals)
- Removed rents >₦100M (mislabeled sales)
- Filtered unrealistic bedroom counts (>20)
- Focused on Lagos State only

**Round 3: Final Quality Control**
- Removed extreme rental outliers
- **Impact**: Max rent dropped from ₦1.5B to ₦50M
- **Result**: Average rent 35% more accurate (₦23M → ₦15M)
- **Final dataset**: 1,993 properties (145 outliers removed)

### 3. Analysis & Visualization (Tableau)

**11 Calculated Fields Created**:
- Sale Price, Annual Rent, Short Let Rate
- Price-to-Rent Ratio (LOD expression)
- Rental Yield % (LOD expression)
- Market Segment, Price Tiers
- Per-Bedroom metrics

**13 Visualizations Built**:
- KPI Dashboard (5 metrics)
- Top 10 Areas (Sales & Rentals)
- Bedroom Demand Analysis
- Investment Opportunity Matrix (Scatter)
- Rental Yield Analysis (Dual-Axis)

**Interactivity**:
- Filter actions (click to drill down)
- Highlight actions (hover to cross-reference)
- Dynamic filters (Area, Property Type, Bedrooms)

---

## 📊 Key Results

### Market Overview
| Metric | Value |
|--------|-------|
| **Total Properties** | 1,993 |
| **For Sale** | 1,144 (57%) |
| **For Rent** | 687 (35%) |
| **Short Let** | 162 (8%) |
| **Avg Sale Price** | ₦580M |
| **Avg Annual Rent** | ₦15M |
| **Median Sale** | ₦290M |
| **Median Rent** | ₦10M |

### Investment Analysis

**🏆 Best ROI Areas**:
1. **Ibeju Lekki**: 10.7x ratio, 9.3% yield
2. **Yaba**: 11x ratio, 9.1% yield
3. **Maryland**: 19.3x ratio, 5.2% yield

**❌ Worst ROI Areas**:
1. **Ikorodu**: 322x ratio, 0.3% yield
2. **Surulere**: 95x ratio, 1.1% yield
3. **Agege**: 78x ratio, 1.3% yield

**💡 Market Leaders**:
- **Lekki**: 936 properties (47% of market!)
- **Ikoyi**: 238 properties (12%)
- **Ajah**: 200 properties (10%)

### Data Quality Improvement
- **Before cleaning**: 2,138 properties, ₦23M avg rent, ₦1,500M max rent
- **After cleaning**: 1,993 properties, ₦15M avg rent, ₦50M max rent
- **Improvement**: 35% more accurate rental analysis

---

## 📈 Visual Outputs

### Dashboard Screenshot
![Lagos Real Estate Dashboard](https://github.com/najibnjidda/lagos-real-estate-analysis/raw/main/assets/dashboard_screenshot.png)

### Key Visualizations

#### 1. Investment Intelligence - Rental Yield Analysis
Shows price-to-rent ratio and rental yield % by area, with quality color-coding (green = good investment, red = poor).

#### 2. Investment Opportunity Matrix
Scatter plot with median lines creating quadrants:
- **Top-Left**: High rent, low price = Best investments
- **Bottom-Right**: Low rent, high price = Avoid

#### 3. Market Breakdown
- **Sales**: Top areas, bedroom demand, price distribution
- **Rentals**: Top areas, bedroom mix by price tier

[**→ View Interactive Dashboard**](https://public.tableau.com/app/profile/najib.njidda/viz/LAGOSREALESTATEMARKETANALYSIS/Dashboard1?publish=yes)

---

## 🔧 Technical Stack

| Component | Technology |
|-----------|------------|
| **Web Scraping** | Python, Playwright, BeautifulSoup |
| **Data Cleaning** | Pandas, Regex |
| **Analysis** | Tableau Desktop |
| **Visualization** | Tableau Public |
| **Version Control** | Git, GitHub |

### Python Libraries
```python
pandas==2.0.3
playwright==1.40.0
beautifulsoup4==4.12.2
```

---

## 🚀 How to Run

### Prerequisites
- Python 3.8 or higher
- Tableau Desktop (for .twbx file) or just use Tableau Public link
- Git

### Step 1: Clone Repository
```bash
git clone https://github.com/najibnjidda/lagos-real-estate-analysis.git
cd lagos-real-estate-analysis
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
playwright install chromium
```

### Step 3: Run Web Scraper (Optional - Data Included)
```bash
python scripts/web_scraping.py
```

This will scrape fresh data from Nigeria Property Centre and save to `data/raw/`.

### Step 4: Clean Data
```bash
python scripts/Lagos_data_cleaning.py
```

This processes raw data and outputs cleaned CSV to `data/processed/lagos_clean_data_3.csv`.

### Step 5: View Dashboard

**Option A**: [View on Tableau Public →](https://public.tableau.com/app/profile/najib.njidda/viz/LAGOSREALESTATEMARKETANALYSIS/Dashboard1?publish=yes)

**Option B**: Open `dashboard/LAGOS_REAL_ESTATE_MARKET_ANALYSIS.twbx` in Tableau Desktop

---

## 📁 Project Structure

```
lagos-real-estate-analysis/
│
├── data/
│   ├── raw/
│   │   └── lagos_raw_data.csv          # Original scraped data (2,138 properties)
│   └── processed/
│       └── lagos_clean_data_3.csv      # Final cleaned data (1,993 properties)
│
├── scripts/
│   ├── web_scraping.py                 # Playwright scraper
│   └── Lagos_data_cleaning.py          # Data cleaning pipeline
│
├── dashboard/
│   └── LAGOS_REAL_ESTATE_MARKET_ANALYSIS.twbx  # Tableau workbook
│
├── assets/
│   └── dashboard_screenshot.png        # Dashboard preview image
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

## 💡 Key Insights

### 1. **Geographic Inequality is Massive**
The **30x variation in ROI** (9.3% vs 0.3%) within the same city is striking. Location matters more than property type or size.

### 2. **Premium ≠ Profitable**
Ikoyi has the highest average sale price (₦1,656M) but only 2.2% yield. High prices don't guarantee good investment returns.

### 3. **Data Quality Matters**
Removing 145 outliers (7% of data) improved rental accuracy by **35%**. This demonstrates the importance of critical thinking in data analysis.

### 4. **Market Concentration**
Lekki's **47% market share** suggests either genuine high demand or potential oversupply. Further investigation needed.

### 5. **Bedroom Sweet Spot**
4-bedroom properties dominate supply (26%) but may not reflect demand. Cross-referencing with sales velocity would provide clearer picture.

---

## 🎓 Conclusion

This project demonstrates **end-to-end data analytics capabilities**:

### What I Delivered:
✅ **Scraped 2,138 properties** from live website  
✅ **Cleaned data through 3 rounds** (35% accuracy improvement)  
✅ **Built 13 interactive visualizations** in Tableau  
✅ **Calculated investment metrics** (ROI, yield, ratios)  
✅ **Delivered actionable insights** for real estate decisions

### Business Impact:
- Helps investors **avoid disasters** (e.g., Ikorodu's 0.3% yield)
- Enables buyers to **benchmark prices** (e.g., "Is ₦500M fair?")
- Provides agents with **data-driven advice**
- Creates **transparency** in opaque market

### What This Proves:
- **Technical Skills**: Python, Pandas, Tableau, LOD expressions, web scraping
- **Business Acumen**: Investment metrics, market analysis, real estate domain knowledge
- **Data Quality Focus**: Iterative cleaning, outlier detection, statistical rigor
- **Communication**: Dashboard design, storytelling with data

---

## 📬 Connect With Me

**Najib Njidda**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/yourprofile)
[![Tableau](https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=tableau&logoColor=white)](https://public.tableau.com/app/profile/najib.njidda)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/najibnjidda)

**Questions or feedback?** Feel free to open an issue or reach out!

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Data source: [Nigeria Property Centre](https://nigeriapropertycentre.com/)
- Inspiration: Need for transparent real estate market intelligence in Lagos
- Tools: Python, Tableau, Playwright

---

**⭐ If you found this project helpful, please give it a star!**

*Last Updated: February 2026*
