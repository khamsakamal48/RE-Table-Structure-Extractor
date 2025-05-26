from bs4 import BeautifulSoup
import pandas as pd

# Load HTML file
with open('RE7Schema/RE7_ACTION_REMINDER.HTML', 'r', encoding='utf-8') as f:
    html = f.read()

# Parse HTML
soup = BeautifulSoup(html, 'html.parser')
tables = soup.find_all('table')

# Convert first table to DataFrame
df = pd.read_html(str(tables[0]))[0]

print(df)