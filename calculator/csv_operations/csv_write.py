"""This module will allow the calculator test to write a log file"""
import pandas as pd
from path_finder import abs_path_to_csv


class CsvWrite:
    """Will turn a pandas dataframe into a csv log file"""
    @staticmethod
    def df_to_csv(df_to_convert, dir_path, file_name):
        """Converts a dataframe into a csv file"""
        pathway = abs_path_to_csv(dir_path)
        df_to_convert.to_csv('{}'.format(file_name) + '.csv')
        return True
