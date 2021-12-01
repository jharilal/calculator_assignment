"""Writes CSV files utilizing pandas"""
import time
from random import randint
import pandas as pd
from calculator.csv_operations.csv_write import CsvWrite
from calculator.history.calculation_history import History


class LogWrite:
    """Contains the methods to prepare a log in a pandas DataFrame"""
    df = pd.DataFrame(columns=['id', 'time', 'operation', 'result', 'filename'])
    zero_df = pd.DataFrame(columns=['id', 'time', 'operation', 'result', 'filename'])
    save_path = 'calculator_assignment/calculator/tests/results'

    @staticmethod
    def get_id():
        """Returns the unique record id of a calculation"""
        record_id = LogWrite.df.shape[0]
        return record_id

    @staticmethod
    def get_time():
        """Returns the current unix time for a calculation"""
        current_time = time.time()
        return current_time

    @staticmethod
    def get_operation():
        """Returns the class of an object. This reflects the object's operation class"""
        curr_operation = type(History.get_last_object())
        return curr_operation

    @staticmethod
    def get_operation_result():
        """Returns the result of a calculation"""
        curr_result = History.last_result()
        return curr_result

    @staticmethod
    def get_filename(test_file_name):
        """Returns the file name of the  csv that is used for a test"""
        return test_file_name

    @staticmethod
    def add_to_log(test_file_name):
        """Conglomerates the methods in the LogWrite class
           to create an entry into the pandas Dataframe"""
        LogWrite.df.loc[LogWrite.df.shape[0]] = [LogWrite.get_id(),
                                                 LogWrite.get_time(),
                                                 LogWrite.get_operation(),
                                                 LogWrite.get_operation_result(),
                                                 LogWrite.get_filename(test_file_name)]
        return True

    @staticmethod
    def add_to_zero_log(test_file_name):
        """Adds an entry to the exceptions log"""
        LogWrite.zero_df.loc[LogWrite.zero_df.shape[0]] = [LogWrite.get_id(),
                                                           LogWrite.get_time(),
                                                           LogWrite.get_operation(),
                                                           LogWrite.get_operation_result(),
                                                           LogWrite.get_filename(test_file_name)]
        return True

    @staticmethod
    def log_filename():
        """Generates a random filename for a log"""
        log_name = 'log_' + str(randint(100, 999))
        return log_name

    @staticmethod
    def zero_log_filename():
        """Generates a random filename for the exceptions log"""
        log_name = 'zero_log_' + str(randint(100, 999))
        return log_name

    @staticmethod
    def reset_dfs():
        """Removes all data from the pandas dataframes"""
        LogWrite.df = pd.DataFrame(columns=['id', 'time', 'operation', 'result', 'filename'])
        LogWrite.zero_df = pd.DataFrame(columns=['id', 'time', 'operation', 'result', 'filename'])
        return True

    @staticmethod
    def commit_log():
        """Commits the finished log into a csv"""
        CsvWrite.df_to_csv(LogWrite.df, file_name=LogWrite.log_filename())
        return True

    @staticmethod
    def commit_zero_log():
        """Commits the finished exceptions log into a csv"""
        CsvWrite.df_to_csv(LogWrite.zero_df, file_name=LogWrite.zero_log_filename())
        return True
