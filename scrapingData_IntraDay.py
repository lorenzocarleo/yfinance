import yfinance as yf

# Define the ticker symbol
tickerSymbol = 'ARMH'

# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get intraday data
intradayDf = tickerData.history(period='1d', interval='1m')  # Example: 1 day of data, 1-minute intervals

# See your data
print(intradayDf)
