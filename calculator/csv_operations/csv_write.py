"""This module will allow the calculator test to write a log file"""
import pandas as pd
import os


class CsvWrite:
    """Will turn a pandas dataframe into a csv log file"""
    @staticmethod
    def df_to_csv(df_to_convert: pd.DataFrame, file_name):
        """Converts a dataframe into a csv file"""
        df_to_convert.to_csv(file_name + ".csv", index=False)
        return True

    @staticmethod
    def set_directory():
        os.chdir('calculator/tests/results')
        return True
