"""Multiplication method that inherits value_a and value_b
   from the calculation class and multiplies the values"""

from calculator.operations.calculation import Calculation


class Multiplication(Calculation):
    """Creates the multiplication object for the Calculator class"""
    def get_result(self):
        """Gets the result of the multiplication object"""
        total_mult = 1
        for item in self.values:
            total_mult *= item
        return round(total_mult, 2)
