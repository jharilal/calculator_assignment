"""Addition method that inherits value_a and value_b from the calculation class"""

from calculator.operations.calculation import Calculation


class Division(Calculation):
    """Creates the division object for the Calculator class"""
    def get_result(self):
        """Gets the result of the division object"""
        total_divide = self.values[0]
        for index, item in enumerate(self.values):
            if item == 0:
                return ZeroDivisionError
            if index > 0:
                total_divide /= item
            else:
                continue
        return total_divide
