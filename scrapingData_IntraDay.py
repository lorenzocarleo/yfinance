import yfinance as yf

# Define the ticker symbol
tickerSymbol = 'AAPL'

# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get intraday data
intradayDf = tickerData.history(period='1d', interval='1m')  # Example: 1 day of data, 1-minute intervals

#Get dataset info
intradayDf.info()

# See your data
print(intradayDf)
intradayDf.to_csv('AAPL.csv')

# Get options expiration dates
options_expirations = tickerData.options

# Check if the desired date is available
desired_date = '2024-01-19'  # Example date, format: 'YYYY-MM-DD'
if desired_date in options_expirations:
    # Fetch options data for the specific date
    options_data = tickerData.option_chain(desired_date)
    calls = options_data.calls  # DataFrame of call options
    puts = options_data.puts    # DataFrame of put options

    #options_data.calls.info()

    print("Call Options Data:\n", calls)
    print("\nPut Options Data:\n", puts)
else:
    print(f"Options data for {desired_date} is not available.")




