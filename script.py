import pandas as pd
import requests
from io import BytesIO
import sqlite3
import csv
pd.options.display.html.table_schema=True
pd.options.display.max_columns=999
pd.options.display.max_rows=999

r = requests.get("https://docs.google.com/spreadsheets/d/1DFUOEk7hUQGfaPW77V2-hGKOCb1QkFirCmUgPsuW_wI/export?format=csv&gid=0")
data = r.content
df = pd.read_csv(BytesIO(data),skiprows = 1)

df['born_day'] = df['born_day'].str.replace(r'[^0-9]','-',regex=True)
df['phone_number'] = df['phone_number'].astype(str)
df['phone_number'] = df['phone_number'].str.replace(r'^62','',regex=True)

conn = sqlite3.connect('data_baskit.db')
df.to_sql('data_baskit', conn, if_exists='replace', index=False)

cursor = conn.cursor()
cursor.execute("SELECT * FROM data_baskit;") # cek table data_baskit
table_baskit = cursor.fetchone()
table_baskit