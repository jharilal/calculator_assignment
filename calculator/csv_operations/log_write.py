"""Writes CSV files utilizing pandas"""
import pandas as pd
import datetime as dt
from csv_write import CsvWrite
from calculator.history.calculation_history import History


class LogWrite:
    """Contains the methods to write a csv from pandas"""
    df = pd.DataFrame(columns=['id', 'time', 'operation', 'result', 'file name'])
    log_number = 0

    @staticmethod
    def get_id():
        record_id = LogWrite.df.shape[0]
        return record_id

    @staticmethod
    def get_time():
        current_time = dt.datetime.utcnow()
        return current_time

    @staticmethod
    def get_operation():
        curr_operation = History.get_last_object()
        return curr_operation

    @staticmethod
    def get_operation_result():
        curr_result = History.last_result()
        return curr_result

    @staticmethod
    def get_filename():
        pass

    @staticmethod
    def add_to_log(df):
        df[df.loc(df.shape[0])] = {'id': LogWrite.get_id(),
                                   'time': LogWrite.get_time(),
                                   'operation': LogWrite.get_operation(),
                                   'result': LogWrite.get_operation_result(),
                                   'filename': LogWrite.get_filename()}
        return True

    @staticmethod
    def log_filename():
        log_name = 'log_' + str(LogWrite.log_number)
        LogWrite.log_number += 1
        return log_name

    @staticmethod
    def reset_df():
        LogWrite.df = pd.DataFrame(columns=['id', 'time', 'operation', 'result', 'filename'])
        return True

    @staticmethod
    def commit_log(df_to_commit):
        CsvWrite.df_to_csv(df_to_commit, 'calculator/tests/results', file_name=LogWrite.log_filename())
        return True
