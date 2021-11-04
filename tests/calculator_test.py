"""Testing the Calculator class"""
import pytest
from calculator.main import Calculator
from calc_history.addition import Addition
from calc_history.division import Division
from calc_history.multiplication import Multiplication


@pytest.fixture
def clear_history():
    """Clears the history of the calculator for each test"""
    Calculator.clear_history()


def test_adding(clear_history):
    """Tests the adding function of the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    assert Calculator.adding(1, 3) == 4


def test_subtracting(clear_history):
    """Tests the subtracting function of the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    assert Calculator.subtracting(6, 3) == 3


def test_multiplying(clear_history):
    """Tests the multiplying function of the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    assert Calculator.multiplying(2, 3) == 6


def test_dividing(clear_history):
    """Tests the dividing function of the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    assert Calculator.dividing(8, 8) == 1
    assert Calculator.dividing(8, 0) == ZeroDivisionError


def test_last_result(clear_history):
    """Tests the last result function for the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    Calculator.dividing(8, 8)
    Calculator.multiplying(2, 3)
    Calculator.adding(2, 3)
    assert Calculator.last_result() == 5


def test_first_result(clear_history):
    """Tests the first result function for the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    Calculator.dividing(8, 8)
    Calculator.multiplying(2, 3)
    Calculator.adding(2, 3)
    assert Calculator.first_result() == 1


def test_last_object(clear_history):
    """Tests the last object function for the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    Calculator.dividing(8, 8)
    Calculator.multiplying(2, 3)
    Calculator.adding(2, 3)
    assert isinstance(Calculator.get_last_object(), Addition) is True


def test_first_object(clear_history):
    """Tests the first object function for the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    Calculator.dividing(8, 8)
    Calculator.multiplying(2, 3)
    Calculator.adding(2, 3)
    assert isinstance(Calculator.get_first_object(), Division) is True


def test_count_history(clear_history):
    """Tests the history count function for the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    Calculator.dividing(8, 8)
    Calculator.multiplying(2, 3)
    Calculator.adding(2, 3)
    assert Calculator.history_count() == 3


def test_clear_history(clear_history):
    """Tests the clear history function for the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    Calculator.dividing(8, 8)
    Calculator.multiplying(2, 3)
    Calculator.adding(2, 3)
    assert Calculator.clear_history() is True
    assert Calculator.history_count() == 0


def test_get_history(clear_history):
    """Tests the get history function for the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument
    Calculator.dividing(8, 8)
    Calculator.multiplying(2, 3)
    Calculator.adding(2, 3)
    assert isinstance(Calculator.get_history()[0], Division) is True
    assert isinstance(Calculator.get_history()[1], Multiplication) is True
    assert isinstance(Calculator.get_history()[2], Addition) is True
