"""This module will allow the calculator test to write a log file"""
import os
import pandas as pd


class CsvWrite:
    """Will turn a pandas dataframe into a csv log file"""
    @staticmethod
    def df_to_csv(df_to_convert: pd.DataFrame):
        """Converts a dataframe into a csv file"""
        df_to_convert.to_csv(path_or_buf=os.path.abspath('calculator/csv_operations/csv_log/applog.csv'),
                             index=False,
                             mode='a',
                             header=False)
        return True

    @staticmethod
    def set_directory(path='calculator/csv_operations/csv_log'):
        """Changes the directory to 'results' in order to commit the logs"""
        if os.getcwd() != os.path.abspath('csv_log'):
            os.chdir(os.path.abspath(path))
        return True
