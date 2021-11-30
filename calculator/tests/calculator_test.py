"""Testing the Calculator class"""
import pytest
from calculator.calculator import Calculator
from calculator.history.calculation_history import History
from calculator.csv_operations.csv_read import CsvRead


@pytest.fixture
def clear_history():
    """Clears the history of the calculator for each test"""
    History.clear_history()


def row_to_tup(row):
    return row['value_a'], row['value_b'], row['value_c']


def test_adding(clear_history):
    """Tests the adding function of the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    df = CsvRead.csv_to_df('calculator/tests/csvs_for_operations/adding_short.csv')
    for index, row in df.iterrows():
        tup = row_to_tup(row)
        assert Calculator.adding(tup) == row['result']  # Testing the short csv for addition

    df_two = CsvRead.csv_to_df('calculator/tests/csvs_for_operations/adding_long.csv')
    for index, row in df_two.iterrows():
        tup = row_to_tup(row)
        assert Calculator.adding(tup) == row['result']  # Testing the long csv for additino


def test_subtracting(clear_history):
    """Tests the subtracting function of the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    df = CsvRead.csv_to_df('calculator/tests/csvs_for_operations/subtracting_short.csv')
    for index, row in df.iterrows():
        tup = row_to_tup(row)
        assert Calculator.subtracting(tup) == row['result']     # Testing the short csv for subtraction

    df_two = CsvRead.csv_to_df('calculator/tests/csvs_for_operations/subtracting_long.csv')
    for index, row in df_two.iterrows():
        tup = row_to_tup(row)
        assert Calculator.subtracting(tup) == row['result']     # Testing the long csv for subtraction


def test_multiplying(clear_history):
    """Tests the multiplying function of the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    df = CsvRead.csv_to_df('calculator/tests/csvs_for_operations/multiplying_short.csv')
    for index, row in df.iterrows():
        tup = row_to_tup(row)
        assert Calculator.multiplying(tup) == row['result']     # Testing the short csv for multiplication

    df_two = CsvRead.csv_to_df('calculator/tests/csvs_for_operations/multiplying_long.csv')
    for index, row in df_two.iterrows():
        tup = row_to_tup(row)
        assert Calculator.multiplying(tup) == row['result']     # Testing the long csv for multiplication


def test_dividing(clear_history):
    """Tests the dividing function of the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    df = CsvRead.csv_to_df('calculator/tests/csvs_for_operations/dividing_short.csv')
    for index, row in df.iterrows():
        tup = row_to_tup(row)
        if row['result'] == '#DIV/0!':
            assert Calculator.dividing(tup) == ZeroDivisionError
        else:
            assert Calculator.dividing(tup) == float(row['result'])  # Testing the short csv for division

    df_two = CsvRead.csv_to_df('calculator/tests/csvs_for_operations/dividing_long.csv')
    for index, row in df_two.iterrows():
        tup = row_to_tup(row)
        if row['result'] == '#DIV/0!':
            assert Calculator.dividing(tup) == ZeroDivisionError
        else:
            assert Calculator.dividing(tup) == float(row['result'])  # Testing the short csv for division
