"""Addition method that inherits value_a and value_b from the calculation class"""

from calculator.operations.calculation import Calculation


class Division(Calculation):
    """Creates the division object for the Calculator class"""
    def get_result(self):
        """Gets the result of the division object"""
        total_divide = self.values[0]
        for index, item in enumerate(self.values):
            if index > 0:
                try:
                    total_divide /= item
                except ZeroDivisionError:
                    return "ZeroDivisionError"
        return round(total_divide, 2)
