import sqlite3

class DatabaseManager :
    def __init__(self, db_path='data.sqlite'):
        self.db_path = db_path

    def connect(self):
        return sqlite3.connect(self.db_path)

    def create_table(self):
        with self.connect() as connection:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS sales (
                    id INT PRIMARY KEY,
                    date TEXT,
                    item_name TEXT,
                    forecasted_units INT,
                    manager_panup INT,
                    day_adjustments INT,
                    total_panup INT,
                    sold_qty INT,
                    leftover_qty INT,
                    target_leftover INT,
                    runout_time INT,
                    missing_qty INT,
                    missing_cost INT
                )
            
            
            
            """)
            connection.commit()

    def test_delete_table(self):
        with self.connect() as connection:
            cursor = connection.cursor()
            cursor.execute("DROP TABLE IF EXISTS sales")
            connection.commit()

    def insert_dataframe(self, df):
        with self.connect() as connection:
            df.to_sql('sales', connection, if_exists='append', index=False)