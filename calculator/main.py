"""Using operation and history functions to build a calculator that can store calculations"""
from calculator.history.calculation_history import History


class Calculator:
    """Initiates a calculator that stores a value"""

    @staticmethod
    def adding(*args):
        """Adds a value to the calculator"""
        History.addition_calculation(*args)
        return History.last_result()

    @staticmethod
    def subtracting(*args):
        """Subtracts a value to the calculator"""
        History.subtraction_calculation(*args)
        return History.last_result()

    @staticmethod
    def multiplying(*args):
        """Multiplies a value to the calculator"""
        History.multiplication_calculation(*args)
        return History.last_result()

    @staticmethod
    def dividing(*args):
        """Divides a value against the calculator"""
        History.division_calculation(*args)
        return History.last_result()
