"""Writes CSV files utilizing pandas"""
import os

import pandas as pd
import time
from calculator.csv_operations.csv_write import CsvWrite
from calculator.history.calculation_history import History
from random import randint


class LogWrite:
    """Contains the methods to write a csv from pandas"""
    df = pd.DataFrame(columns=['id', 'time', 'operation', 'result', 'filename'])
    zero_df = pd.DataFrame(columns=['id', 'time', 'operation', 'result', 'filename'])
    save_path = 'calculator_assignment/calculator/tests/results'

    @staticmethod
    def get_id():
        record_id = LogWrite.df.shape[0]
        return record_id

    @staticmethod
    def get_time():
        current_time = time.time()
        return current_time

    @staticmethod
    def get_operation():
        curr_operation = type(History.get_last_object())
        return curr_operation

    @staticmethod
    def get_operation_result():
        curr_result = History.last_result()
        return curr_result

    @staticmethod
    def get_filename(test_file_name):
        return test_file_name

    @staticmethod
    def add_to_log(test_file_name):
        LogWrite.df.loc[LogWrite.df.shape[0]] = [LogWrite.get_id(),
                                                 LogWrite.get_time(),
                                                 LogWrite.get_operation(),
                                                 LogWrite.get_operation_result(),
                                                 LogWrite.get_filename(test_file_name)]
        return True

    @staticmethod
    def add_to_zero_log(test_file_name):
        LogWrite.zero_df.loc[LogWrite.zero_df.shape[0]] = {'id': LogWrite.get_id(),
                                                           'time': LogWrite.get_time(),
                                                           'operation': LogWrite.get_operation(),
                                                           'result': LogWrite.get_operation_result(),
                                                           'filename': LogWrite.get_filename(test_file_name)}
        return True

    @staticmethod
    def log_filename():
        log_name = 'log_' + str(randint(1, 10))
        return log_name

    @staticmethod
    def zero_log_filename():
        log_name = 'zero_log_' + str(randint(1, 10))
        return log_name

    @staticmethod
    def reset_dfs():
        LogWrite.df = pd.DataFrame(columns=['id', 'time', 'operation', 'result', 'filename'])
        LogWrite.zero_df = pd.DataFrame(columns=['id', 'time', 'operation', 'result', 'filename'])
        return True

    @staticmethod
    def commit_log():
        print(os.getcwd())
        CsvWrite.df_to_csv(LogWrite.df, file_name=LogWrite.log_filename())
        return True

    @staticmethod
    def commit_zero_log():
        print(os.getcwd())
        CsvWrite.df_to_csv(LogWrite.zero_df, file_name=LogWrite.zero_log_filename())
        return True
