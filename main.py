from data_processing import DataProcessor
from database import DatabaseManager
import glob

rows_to_trim = ['Bagels', 'Totals:', 'Breads', 'Souffles', 'Sweets']

if __name__ == '__main__':
    dp = DataProcessor('2.5.2025.xlsx', rows_to_trim)
    db = DatabaseManager()
