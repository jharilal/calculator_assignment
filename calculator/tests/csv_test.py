from calculator.csv_operations.csv_read import CsvRead


def test_csv_read():
    df = CsvRead.csv_to_df('calculator/tests/csvs_for_operations/subtracting_short.csv')
    for index, row in df.iterrows():
        print(row['value_a'])


