import os
import requests
import pandas as pd
import yfinance as yf

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

def save_stock(ticker, filename):
    df = yf.Ticker(ticker).history(period="max").reset_index()
    df.to_csv(os.path.join(DATA_DIR, filename), index=False)
    print(filename, "rows:", len(df))

def save_revenue(url, filename, match_text):
    html = requests.get(url, timeout=30).text
    table = pd.read_html(html, match=match_text)[0].iloc[:, :2]
    table.columns = ["Date", "Revenue"]
    table["Revenue"] = (
        table["Revenue"].astype(str)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
    )
    table["Revenue"] = pd.to_numeric(table["Revenue"], errors="coerce")
    table.dropna(inplace=True)
    table.to_csv(os.path.join(DATA_DIR, filename), index=False)
    print(filename, "rows:", len(table))

save_stock("TSLA", "tesla_stock.csv")
save_stock("GME", "gamestop_stock.csv")

save_revenue(
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm",
    "tesla_revenue.csv",
    "Tesla Quarterly Revenue"
)

save_revenue(
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html",
    "gamestop_revenue.csv",
    "GameStop Quarterly Revenue"
)
