"""Addition method that inherits value_a and value_b from the calculation class"""

from calculator.operations.calculation import Calculation


class Division(Calculation):
    """Creates the division object for the Calculator class"""
    def get_result(self):
        """Gets the result of the division object"""
        if self.value_b == 0:
            return ZeroDivisionError
        return self.value_a / self.value_b
