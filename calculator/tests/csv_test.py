"""Tests the csv operation functions"""

from calculator.csv_operations.csv_read import CsvRead


def test_csv_read():
    """Tests the csv_read function"""
    # pylint: disable=('invalid-name')
    df = CsvRead.csv_to_df('calculator/tests/csvs_for_operations/subtracting_short.csv')
    for row in df.iterrows():
        print(row['value_a'])
