"""Addition method that inherits value_a and value_b from the calculation class"""

from calculator.operations.calculation import Calculation


class Subtraction(Calculation):
    """Creates the subtraction object for the Calculator class"""
    def get_result(self):
        """Gets the result of the subtraction object"""
        total_sub = 0
        for item in self.values:
            total_sub -= item
        return total_sub
