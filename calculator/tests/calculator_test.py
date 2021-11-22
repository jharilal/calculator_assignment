"""Testing the Calculator class"""
import pytest
from calculator.main import Calculator
from calculator.history.calculation_history import History
from calculator.operations.addition import Addition
from calculator.operations.division import Division
from calculator.operations.multiplication import Multiplication
from calculator.csv_operations.csv_read import CsvRead


@pytest.fixture
def clear_history():
    """Clears the history of the calculator for each test"""
    History.clear_history()


def test_adding(clear_history):
    """Tests the adding function of the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    tup = (3, 4, 5)                     # Arrange
    result = Calculator.adding(tup)     # Act
    assert result == 12                 # Assert


def test_subtracting(clear_history):
    """Tests the subtracting function of the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    df = CsvRead.csv_to_df('calculator/tests/csvs_for_operations/subtracting_short.csv')
    for index, row in df.iterrows():
        tup = (row['value_a'], row['value_b'], row['value_c'])
        assert Calculator.subtracting(tup) == row['result']


def test_multiplying(clear_history):
    """Tests the multiplying function of the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    tup = (0, 3, 2)
    tup_two = (4, 3, 2)
    Calculator.multiplying(tup)
    result = History.last_result()
    Calculator.multiplying(tup_two)
    result_two = History.last_result()
    assert result == 0
    assert result_two == 24


def test_dividing(clear_history):
    """Tests the dividing function of the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    tup_one = (24, 2, 3)
    tup_two = (0, 2, 3)
    tup_three = (2, 0, 3)
    result_one = Calculator.dividing(tup_one)
    result_two = Calculator.dividing(tup_two)
    result_three = Calculator.dividing(tup_three)
    assert result_one == 4
    assert result_two == ZeroDivisionError
    assert result_three == ZeroDivisionError


def test_last_result(clear_history):
    """Tests the last result function for the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    tup = (12, 4)
    assert Calculator.dividing(tup) == 3
    assert Calculator.multiplying(tup) == 48
    assert Calculator.adding(tup) == 16
    assert History.last_result() == 16


def test_first_result(clear_history):
    """Tests the first result function for the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    tup = (12, 4)
    assert Calculator.dividing(tup) == 3
    assert Calculator.multiplying(tup) == 48
    assert Calculator.adding(tup) == 16
    assert History.first_result() == 3


def test_last_object(clear_history):
    """Tests the last object function for the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    tup = (12, 4)
    assert Calculator.dividing(tup) == 3
    assert Calculator.multiplying(tup) == 48
    assert Calculator.adding(tup) == 16
    assert isinstance(History.get_last_object(), Addition) is True


def test_first_object(clear_history):
    """Tests the first object function for the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    tup = (12, 4)
    assert Calculator.dividing(tup) == 3
    assert Calculator.multiplying(tup) == 48
    assert Calculator.adding(tup) == 16
    assert isinstance(History.get_first_object(), Division) is True


def test_count_history(clear_history):
    """Tests the history count function for the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    assert History.history_count() == 0
    tup = (12, 4)
    assert Calculator.dividing(tup) == 3
    assert Calculator.multiplying(tup) == 48
    assert Calculator.adding(tup) == 16
    assert History.history_count() == 3


def test_clear_history(clear_history):
    """Tests the clear history function for the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    tup = (12, 4)
    assert Calculator.dividing(tup) == 3
    assert Calculator.multiplying(tup) == 48
    assert Calculator.adding(tup) == 16
    assert History.clear_history() is True
    assert History.history_count() == 0


def test_get_history(clear_history):
    """Tests the get history function for the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    tup = (12, 4)
    assert Calculator.dividing(tup) == 3
    assert Calculator.multiplying(tup) == 48
    assert Calculator.adding(tup) == 16
    assert isinstance(History.get_history()[0], Division) is True
    assert isinstance(History.get_history()[1], Multiplication) is True
    assert isinstance(History.get_history()[2], Addition) is True
