"""Addition method that inherits value_a and value_b from the calculation class"""

from calculator.operations.calculation import Calculation


class Multiplication(Calculation):
    """Creates the multiplication object for the Calculator class"""
    def get_result(self):
        """Gets the result of the multiplication object"""
        return self.value_a * self.value_b
