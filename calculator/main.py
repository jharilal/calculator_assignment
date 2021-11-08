"""Using operation and history functions to build a calculator that can store calculations"""
from calculator.operations.addition import Addition
from calculator.operations.subtraction import Subtraction
from calculator.operations.multiplication import Multiplication
from calculator.operations.division import Division
from calculator.history.calculation_history import History


class Calculator:
    """Initiates a calculator that stores a value"""

    @staticmethod
    def adding(*args):
        """Adds a value to the calculator"""
        addition = Addition(args)
        History.append_to_history(addition)
        return History.last_result()

    @staticmethod
    def subtracting(*args):
        """Subtracts a value to the calculator"""
        subtraction = Subtraction(args)
        History.append_to_history(subtraction)
        return History.last_result()

    @staticmethod
    def multiplying(*args):
        """Multiplies a value to the calculator"""
        multiplication = Multiplication(args)
        History.append_to_history(multiplication)
        return History.last_result()

    @staticmethod
    def dividing(*args):
        """Divides a value against the calculator"""
        division = Division(args)
        History.append_to_history(division)
        return History.last_result()
