import yfinance as yf
from datetime import datetime, date

# Constants
TICKER_SYMBOL = "DDOG"
START_YEAR = 2020
END_YEAR = 2025
MONTHS_IN_YEAR = 12
PRICE_FORMAT = "${:.2f}"
DATE_FORMAT = "%Y-%m-%d"
MONTH_NAME_FORMAT = "%B"
FIRST_DAY_OF_MONTH = "01"
TRADE_VALUE_COLUMN = "TradeValue"
CLOSE_COLUMN = "Close"
VOLUME_COLUMN = "Volume"
FUTURE_DATE_MESSAGE = "Future date"
NO_DATA_MESSAGE = "No data available"
ERROR_MESSAGE = "Error - {}"
YEAR_HEADER = "=== {} ==="
MONTH_PRICE_FORMAT = "{}: {}"

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
    
    if data.empty:
        return None
        
    # Calculate the daily traded value (Close * Volume)
    data[TRADE_VALUE_COLUMN] = data[CLOSE_COLUMN] * data[VOLUME_COLUMN]
    # Compute VWAP as total traded value divided by total volume
    vwap = data[TRADE_VALUE_COLUMN].sum() / data[VOLUME_COLUMN].sum()
    
    return vwap

if __name__ == "__main__":
    # Calculate VWAP for each month from 2020 to 2025
    years = range(START_YEAR, END_YEAR + 1)
    months = range(1, MONTHS_IN_YEAR + 1)  # All months
    current_date = date.today()
    
    for year in years:
        print(YEAR_HEADER.format(year))
        for month in months:
            # Skip future dates
            if year > current_date.year or (year == current_date.year and month > current_date.month):
                month_name = datetime(year, month, 1).strftime(MONTH_NAME_FORMAT)
                print(MONTH_PRICE_FORMAT.format(month_name, FUTURE_DATE_MESSAGE))
                continue
                
            # Get the last day of the month
            if month == MONTHS_IN_YEAR:
                next_month = 1
                next_year = year + 1
            else:
                next_month = month + 1
                next_year = year
            
            start_date = f"{year}-{month:02d}-{FIRST_DAY_OF_MONTH}"
            end_date = f"{next_year}-{next_month:02d}-{FIRST_DAY_OF_MONTH}"
            
            try:
                vwap = calculate_vwap(TICKER_SYMBOL, start_date, end_date)
                month_name = datetime(year, month, 1).strftime(MONTH_NAME_FORMAT)
                if vwap is not None:
                    print(MONTH_PRICE_FORMAT.format(month_name, PRICE_FORMAT.format(vwap)))
                else:
                    print(MONTH_PRICE_FORMAT.format(month_name, NO_DATA_MESSAGE))
            except Exception as e:
                print(MONTH_PRICE_FORMAT.format(month_name, ERROR_MESSAGE.format(str(e))))