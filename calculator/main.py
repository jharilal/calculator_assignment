"""Main function to initiate the calculator_test.py file"""

from time import sleep
import pytest
from calculator.csv_operations.path_finder import abs_path_to_csv
from calculator.csv_operations.csv_write import CsvWrite
from calculator.csv_operations.log_write import LogWrite

print('The purpose of this file is to test the calculator for functionality.')


def main():


    print("Converting log dataframe into csv...")
    CsvWrite.df_to_csv(LogWrite.df)
    sleep(3)
    print("Resetting dataframe for new log...")
    LogWrite.reset_df()
    print("Test complete")


if __name__ == '__main__':
    main()
