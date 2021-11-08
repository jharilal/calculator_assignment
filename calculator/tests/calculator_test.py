"""Testing the Calculator class"""
import pytest
from calculator.main import Calculator, History
from calculator.operations.addition import Addition
from calculator.operations.division import Division
from calculator.operations.multiplication import Multiplication


@pytest.fixture
def clear_history():
    """Clears the history of the calculator for each test"""
    History.clear_history()


def test_adding(clear_history):
    """Tests the adding function of the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    assert History.clear_history() is True
    assert Calculator.adding(1, 3) == 4
    assert Calculator.adding(2, 3) == 5
    assert Calculator.adding(3, 3) == 6
    assert Calculator.adding(4, 3) == 7


def test_subtracting(clear_history):
    """Tests the subtracting function of the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    assert History.clear_history() is True
    assert Calculator.subtracting(6, 3) == 3
    assert Calculator.subtracting(5, 3) == 2
    assert Calculator.subtracting(4, 3) == 1
    assert Calculator.subtracting(3, 3) == 0


def test_multiplying(clear_history):
    """Tests the multiplying function of the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    assert History.clear_history() is True
    assert Calculator.multiplying(0, 3) == 0
    assert Calculator.multiplying(1, 3) == 3
    assert Calculator.multiplying(2, 3) == 6
    assert Calculator.multiplying(3, 3) == 9


def test_dividing(clear_history):
    """Tests the dividing function of the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    assert History.clear_history() is True
    assert Calculator.dividing(8, 8) == 1
    assert Calculator.dividing(8, 4) == 2
    assert Calculator.dividing(8, 2) == 4
    assert Calculator.dividing(8, 0) == ZeroDivisionError


def test_last_result(clear_history):
    """Tests the last result function for the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    assert History.clear_history() is True
    assert Calculator.dividing(8, 8) == 1
    assert Calculator.multiplying(2, 3) == 6
    assert Calculator.adding(2, 3) == 5
    assert History.last_result() == 5


def test_first_result(clear_history):
    """Tests the first result function for the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    assert History.clear_history() is True
    assert Calculator.dividing(8, 8) == 1
    assert Calculator.multiplying(2, 3) == 6
    assert Calculator.adding(2, 3) == 5
    assert History.first_result() == 1


def test_last_object(clear_history):
    """Tests the last object function for the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    assert History.clear_history() is True
    assert Calculator.dividing(8, 8) == 1
    assert Calculator.multiplying(2, 3) == 6
    assert Calculator.adding(2, 3) == 5
    assert isinstance(History.get_last_object(), Addition) is True


def test_first_object(clear_history):
    """Tests the first object function for the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    assert History.clear_history() is True
    assert Calculator.dividing(8, 8) == 1
    assert Calculator.multiplying(2, 3) == 6
    assert Calculator.adding(2, 3) == 5
    assert isinstance(History.get_first_object(), Division) is True


def test_count_history(clear_history):
    """Tests the history count function for the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    assert History.clear_history() is True
    assert History.history_count() == 0
    assert Calculator.dividing(8, 8) == 1
    assert Calculator.multiplying(2, 3) == 6
    assert Calculator.adding(2, 3) == 5
    assert History.history_count() == 3


def test_clear_history(clear_history):
    """Tests the clear history function for the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    assert History.clear_history() is True
    assert Calculator.dividing(8, 8) == 1
    assert Calculator.multiplying(2, 3) == 6
    assert Calculator.adding(2, 3) == 5
    assert History.clear_history() is True
    assert History.history_count() == 0


def test_get_history(clear_history):
    """Tests the get history function for the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    assert History.clear_history() is True
    assert Calculator.dividing(8, 8) == 1
    assert Calculator.multiplying(2, 3) == 6
    assert Calculator.adding(2, 3) == 5
    assert isinstance(History.get_history()[0], Division) is True
    assert isinstance(History.get_history()[1], Multiplication) is True
    assert isinstance(History.get_history()[2], Addition) is True
