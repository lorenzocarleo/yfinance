import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of Yahoo Finance Earnings Calendar
url = 'https://finance.yahoo.com/calendar/earnings'

# Send a request to the URL
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table containing the earnings data
earnings_table = soup.find('table', class_='W(100%)')

# Parse table rows and extract Symbol data
rows = earnings_table.find_all('tr')[1:]  # Skip the header row
symbols = []

for row in rows:
    cols = row.find_all('td')
    symbol = cols[0].text.strip()  # Extract the symbol
    symbols.append(symbol)

# Convert the list of symbols to a DataFrame
symbols_df = pd.DataFrame(symbols, columns=['Symbol'])

print(symbols_df)

symbols_df.to_csv("ticker_symbols.csv", index=False)

