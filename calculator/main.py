"""Creating a calculator"""
from calc_history.addition import Addition
from calc_history.subtraction import Subtraction
from calc_history.multiplication import Multiplication
from calc_history.division import Division


class Calculator:
    """Initiates a calculator that stores a value"""
    history =[]

    @staticmethod
    def append_to_history(result):
        """Adds a calculation object to the history"""
        Calculator.history.append(result)
        return True

    @staticmethod
    def last_result():
        """Returns the most recent result of the calculator history"""
        return Calculator.history[-1].get_result()

    @staticmethod
    def get_last_object():
        """Returns the most recent object of the calculator history"""
        return Calculator.history[-1]

    @staticmethod
    def first_result():
        """Returns the first result of the calculator history"""
        return Calculator.history[0].get_result()

    @staticmethod
    def get_first_object():
        """Returns the first object of the calculator history"""
        return Calculator.history[0]

    @staticmethod
    def history_count():
        """Returns the total number of calculation objects in the history"""
        return len(Calculator.history)

    @staticmethod
    def get_history():
        """Returns a list of calculation objects"""
        return Calculator.history

    @staticmethod
    def clear_history():
        """Removes all calculations from the calculation history"""
        Calculator.history = []
        return True

    @staticmethod
    def adding(value_a, value_b):
        """Adds a value to the calculator"""
        addition = Addition.create(value_a, value_b)
        Calculator.append_to_history(addition)
        return Calculator.last_result()

    @staticmethod
    def subtracting(value_a, value_b):
        """Subtracts a value to the calculator"""
        subtraction = Subtraction.create(value_a, value_b)
        Calculator.append_to_history(subtraction)
        return Calculator.last_result()

    @staticmethod
    def multiplying(value_a, value_b):
        """Multiplies a value to the calculator"""
        multiplication = Multiplication.create(value_a, value_b)
        Calculator.append_to_history(multiplication)
        return Calculator.last_result()

    @staticmethod
    def dividing(value_a, value_b):
        """Divides a value against the calculator"""
        division = Division.create(value_a, value_b)
        Calculator.append_to_history(division)
        return Calculator.last_result()
