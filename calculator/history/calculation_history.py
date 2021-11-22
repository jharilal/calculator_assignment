"""Holds the history class and history operations for the calculator"""
from calculator.operations.addition import Addition
from calculator.operations.subtraction import Subtraction
from calculator.operations.multiplication import Multiplication
from calculator.operations.division import Division


class History:
    """Holds the methods for history operations on the calculator"""
    history = []

    @staticmethod
    def append_to_history(result):
        """Adds a calculation object to the history"""
        History.history.append(result)
        return True

    @staticmethod
    def last_result():
        """Returns the most recent result of the calculator history"""
        return History.history[-1].get_result()

    @staticmethod
    def get_last_object():
        """Returns the most recent object of the calculator history"""
        return History.history[-1]

    @staticmethod
    def first_result():
        """Returns the first result of the calculator history"""
        return History.history[0].get_result()

    @staticmethod
    def get_first_object():
        """Returns the first object of the calculator history"""
        return History.history[0]

    @staticmethod
    def history_count():
        """Returns the total number of calculation objects in the history"""
        return len(History.history)

    @staticmethod
    def get_history():
        """Returns a list of calculation objects"""
        return History.history

    @staticmethod
    def clear_history():
        """Removes all calculations from the calculation history"""
        History.history = []
        return True

    @staticmethod
    def addition_calculation(values):
        """Creates an addition calculation object"""
        History.append_to_history(Addition.create(values))
        return True

    @staticmethod
    def subtraction_calculation(values):
        """Creates an addition calculation object"""
        History.append_to_history(Subtraction.create(values))
        return True

    @staticmethod
    def multiplication_calculation(values):
        """Creates an addition calculation object"""
        History.append_to_history(Multiplication.create(values))
        return True

    @staticmethod
    def division_calculation(values):
        """Creates an addition calculation object"""
        History.append_to_history(Division.create(values))
        return True
