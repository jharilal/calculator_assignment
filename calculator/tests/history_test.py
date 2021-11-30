"""Testing the Calculator class"""
import pytest
from calculator.calculator import Calculator
from calculator.history.calculation_history import History
from calculator.operations.addition import Addition
from calculator.operations.division import Division
from calculator.operations.multiplication import Multiplication


@pytest.fixture
def clear_history():
    """Clears the history of the calculator for each test"""
    History.clear_history()


def row_to_tup(row):
    """Returns the format for the row within a datafram"""
    return row['value_a'], row['value_b'], row['value_c']


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
