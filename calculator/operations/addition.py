"""Addition method that inherits value_a and value_b from the calculation class"""

from calculator.operations.calculation import Calculation


class Addition(Calculation):
    """Creates the addition object for the Calculator class"""
    def get_result(self):
        """Gets the result of the addition object"""
        sum_of_values = 0
        for item in self.values:
            sum_of_values += item
        return sum_of_values
