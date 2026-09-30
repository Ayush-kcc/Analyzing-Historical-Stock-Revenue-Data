# Analyzing Historical Stock/Revenue Data and Building a Dashboard

This portfolio project analyzes Tesla (TSLA) and GameStop (GME) historical stock price and revenue data using Python, yfinance, web scraping, Pandas, BeautifulSoup, and Plotly.

## Repository structure

```text
Analyzing-Historical-Stock-Revenue-Data/
├── Analyzing_Historical_Stock_Revenue_Data_and_Building_a_Dashboard.ipynb
├── README.md
├── requirements.txt
├── download_datasets.py
└── data/
    ├── tesla_stock.csv
    ├── tesla_revenue.csv
    ├── gamestop_stock.csv
    └── gamestop_revenue.csv
```

## What I practiced

- Historical stock-data extraction with yfinance
- Web scraping with requests and BeautifulSoup
- Data cleaning with Pandas
- Time-series analysis
- Interactive Plotly visualization
- Building a reusable stock/revenue dashboard

## Data sources

- Stock price data: Yahoo Finance via yfinance (`TSLA`, `GME`)
- Revenue data: IBM Skills Network course-hosted HTML pages used for the assignment

## Generate fresh/full data

The CSVs included here are preview snapshots. To regenerate full stock histories and the revenue tables from the source pages, run:

```bash
pip install -r requirements.txt
python download_datasets.py
```

## Run the notebook

```bash
jupyter notebook
```

Open the `.ipynb` file and run cells from top to bottom.
