import pandas as pd


class DataProcessor:
    def __init__(self, filepath, trimrows):
        self.filepath = filepath
        self.trimrows = trimrows

    def load_data(self):
        df = pd.read_excel(self.filepath, sheet_name='Detail', header=None)
        date_text = df.at[3, 0]
        date = date_text[15:]
        df = df.iloc[14:]
        df.loc[:, 'Date'] = date
        df = df.rename(columns={0: 'Target Leftover', 1: 'Forecast', 2: 'Product', 3: 'Pan-up', 4: 'Adjustments',
                                5: 'Total Pan-up', 6: 'Sold', 7: 'Leftover', 8: 'Runout Time', 9: 'Missing Qty',
                                10: 'Missing Cost'})
        df = df.reindex(
            columns=['Date', 'Product', 'Forecast', 'Pan-up', 'Adjustments', 'Total Pan-up', 'Sold', 'Leftover',
                     'Target Leftover', 'Runout Time', 'Missing Qty', 'Missing Cost'])
        df = df[~df['Product'].isin(self.trimrows)]
        return df
