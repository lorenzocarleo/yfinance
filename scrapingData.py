import yfinance as yf

# Define the ticker symbol
tickerSymbol = 'BKUH'

# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this ticker
tickerDf = tickerData.history(period='1mo', interval='1d')  # Example: 1 month of data

# See your data
print(tickerDf)
