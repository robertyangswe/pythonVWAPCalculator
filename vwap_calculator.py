import yfinance as yf
from datetime import datetime

def calculate_vwap(ticker_symbol, start_date, end_date):
    """
    Calculate the Volume Weighted Average Price (VWAP) for a given ticker and date range.
    
    Args:
        ticker_symbol (str): The stock ticker symbol (e.g., "DDOG")
        start_date (str): Start date in YYYY-MM-DD format
        end_date (str): End date in YYYY-MM-DD format
    
    Returns:
        float: The VWAP for the specified period
    """
    ticker = yf.Ticker(ticker_symbol)
    data = ticker.history(start=start_date, end=end_date)
    
    # Calculate the daily traded value (Close * Volume)
    data["TradeValue"] = data["Close"] * data["Volume"]
    # Compute VWAP as total traded value divided by total volume
    vwap = data["TradeValue"].sum() / data["Volume"].sum()
    
    return vwap

if __name__ == "__main__":
    # Calculate VWAP for each month from 2020 to 2025
    years = range(2020, 2026)
    months = range(4, 5)
    
    for year in years:
        print(f"\n=== {year} ===")
        for month in months:
            # Get the last day of the month
            if month == 12:
                next_month = 1
                next_year = year + 1
            else:
                next_month = month + 1
                next_year = year
            
            start_date = f"{year}-{month:02d}-01"
            end_date = f"{next_year}-{next_month:02d}-01"
            
            try:
                vwap = calculate_vwap("DDOG", start_date, end_date)
                month_name = datetime(year, month, 1).strftime('%B')
                print(f"{month_name}: ${vwap:.2f}")
            except Exception as e:
                print(f"{month_name}: No data available")