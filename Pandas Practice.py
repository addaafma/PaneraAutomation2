import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

rows_to_trim = ['Bagels', 'Totals:', 'Breads', 'Souffles', 'Sweets']

df = pd.read_excel("2.5.2025.xlsx", sheet_name='Detail', header=None)
date_text = df.at[3, 0]
date = date_text[15:]
df = df.iloc[14:]
df.loc[:, 'Date'] = date
df = df.rename(columns={0 : 'Target Leftover', 1 : 'Forecast', 2 : 'Product', 3 : 'Pan-up', 4 : 'Adjustments', 5 : 'Total Pan-up', 6 : 'Sold', 7 : 'Leftover', 8 : 'Runout Time', 9 : 'Missing Qty', 10 : 'Missing Cost' })
df = df.reindex(columns=['Date', 'Product', 'Forecast', 'Pan-up', 'Adjustments', 'Total Pan-up', 'Sold', 'Leftover', 'Target Leftover', 'Runout Time', 'Missing Qty', 'Missing Cost'])
df = df[~df['Product'].isin(rows_to_trim)]

df.to_excel("2.5.2025 edited.xlsx", index=False)
