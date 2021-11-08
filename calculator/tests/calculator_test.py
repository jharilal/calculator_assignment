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
    assert Calculator.adding(3, 4, 5) == 12


def test_subtracting(clear_history):
    """Tests the subtracting function of the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    assert Calculator.subtracting(6, 3, 2) == -11


def test_multiplying(clear_history):
    """Tests the multiplying function of the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    assert Calculator.multiplying(0, 3, 2) == 0
    assert Calculator.multiplying(4, 3, 2) == 24


def test_dividing(clear_history):
    """Tests the dividing function of the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    assert Calculator.dividing(24, 2, 3) == 4
    assert Calculator.dividing(0, 2, 3) == ZeroDivisionError
    assert Calculator.dividing(2, 0, 3) == ZeroDivisionError


def test_last_result(clear_history):
    """Tests the last result function for the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    assert Calculator.dividing(8, 8) == 1
    assert Calculator.multiplying(2, 3) == 6
    assert Calculator.adding(2, 3) == 5
    assert History.last_result() == 5


def test_first_result(clear_history):
    """Tests the first result function for the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    assert Calculator.dividing(8, 8) == 1
    assert Calculator.multiplying(2, 3) == 6
    assert Calculator.adding(2, 3) == 5
    assert History.first_result() == 1


def test_last_object(clear_history):
    """Tests the last object function for the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    assert Calculator.dividing(8, 8) == 1
    assert Calculator.multiplying(2, 3) == 6
    assert Calculator.adding(2, 3) == 5
    assert isinstance(History.get_last_object(), Addition) is True


def test_first_object(clear_history):
    """Tests the first object function for the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    assert Calculator.dividing(8, 8) == 1
    assert Calculator.multiplying(2, 3) == 6
    assert Calculator.adding(2, 3) == 5
    assert isinstance(History.get_first_object(), Division) is True


def test_count_history(clear_history):
    """Tests the history count function for the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    assert History.history_count() == 0
    assert Calculator.dividing(8, 8) == 1
    assert Calculator.multiplying(2, 3) == 6
    assert Calculator.adding(2, 3) == 5
    assert History.history_count() == 3


def test_clear_history(clear_history):
    """Tests the clear history function for the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    assert Calculator.dividing(8, 8) == 1
    assert Calculator.multiplying(2, 3) == 6
    assert Calculator.adding(2, 3) == 5
    assert History.clear_history() is True
    assert History.history_count() == 0


def test_get_history(clear_history):
    """Tests the get history function for the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    assert Calculator.dividing(8, 8) == 1
    assert Calculator.multiplying(2, 3) == 6
    assert Calculator.adding(2, 3) == 5
    assert isinstance(History.get_history()[0], Division) is True
    assert isinstance(History.get_history()[1], Multiplication) is True
    assert isinstance(History.get_history()[2], Addition) is True
