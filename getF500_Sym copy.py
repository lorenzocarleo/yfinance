from bs4 import BeautifulSoup
import requests
import pandas as pd

# URL of Yahoo Finance Earnings Calendar
url = 'https://finance.yahoo.com/calendar/earnings'

# Send a request to the URL
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table containing the earnings data
earnings_table = soup.find('table', class_='W(100%)')

# Parse table rows and extract data
rows = earnings_table.find_all('tr')[1:]  # Skip the header row
earnings_data = []

for row in rows:
    cols = row.find_all('td')
    earnings_data.append({
        'Symbol': cols[0].text.strip(),
        'Company': cols[1].text.strip(),
        'Earnings Call Time': cols[2].text.strip(),
        'EPS Estimate': cols[3].text.strip(),
        'Reported EPS': cols[4].text.strip(),
        'Surprise(%)': cols[5].text.strip()
    })

# Convert the data to a DataFrame
df = pd.DataFrame(earnings_data)

df.head()  # Display the first few rows

df.to_csv("Fyfinance/500list.csv")

print (df)


