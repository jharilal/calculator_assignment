"""Testing the Calculator class"""
import pytest
from calculator.calculator import Calculator
from calculator.history.calculation_history import History
from calculator.csv_operations.csv_read import CsvRead
from calculator.csv_operations.log_write import LogWrite
from calculator.csv_operations.csv_write import CsvWrite
from calculator.csv_operations.file_operator import FileOperator


@pytest.fixture
def clear_history():
    """Clears the history of the calculator for each test"""
    History.clear_history()


def row_to_tup(row):
    return row['value_a'], row['value_b'], row['value_c']


def test_adding(clear_history):
    """Tests the adding function of the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    test_file_name = 'adding_long.csv'
    csv_loc = CsvRead.search_csv(test_file_name)
    df_two = CsvRead.csv_to_df(csv_loc)
    for index, row in df_two.iterrows():
        tup = row_to_tup(row)
        test_value = Calculator.adding(tup)
        LogWrite.add_to_log(test_file_name)
        assert test_value == row['result']  # Testing the long csv for adding
    FileOperator.move_to_destination(csv_loc)



def test_subtracting(clear_history):
    """Tests the subtracting function of the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    test_file_name = 'subtracting_long.csv'
    csv_loc = CsvRead.search_csv(test_file_name)
    df_two = CsvRead.csv_to_df(csv_loc)
    for index, row in df_two.iterrows():
        tup = row_to_tup(row)
        assert Calculator.subtracting(tup) == row['result']     # Testing the long csv for subtraction
        LogWrite.add_to_log(test_file_name)
    FileOperator.move_to_destination(csv_loc)


def test_multiplying(clear_history):
    """Tests the multiplying function of the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    test_file_name = 'multiplying_long.csv'
    csv_loc = CsvRead.search_csv(test_file_name)
    df_two = CsvRead.csv_to_df(csv_loc)
    for index, row in df_two.iterrows():
        tup = row_to_tup(row)
        assert Calculator.multiplying(tup) == row['result']     # Testing the long csv for multiplication
        LogWrite.add_to_log(test_file_name)
    FileOperator.move_to_destination(csv_loc)


def test_dividing(clear_history):
    """Tests the dividing function of the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    test_file_name = 'dividing_long.csv'
    csv_loc = CsvRead.search_csv(test_file_name)
    df_two = CsvRead.csv_to_df(csv_loc)
    for index, row in df_two.iterrows():
        tup = row_to_tup(row)
        if row['result'] == '#DIV/0!':
            assert Calculator.dividing(tup) == ZeroDivisionError
            LogWrite.add_to_zero_log(test_file_name)
        else:
            assert Calculator.dividing(tup) == float(row['result'])  # Testing the short csv for division
            LogWrite.add_to_log(test_file_name)
    FileOperator.move_to_destination(csv_loc)


def test_complete_logs():
    CsvWrite.set_directory()
    LogWrite.commit_log()
    LogWrite.commit_zero_log()
    LogWrite.reset_dfs()
