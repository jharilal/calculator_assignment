"""Addition method that inherits value_a and value_b from the calculation class"""

from calc_history.calculation import Calculation


class Addition(Calculation):
    """Creates the addition object for the Calculator class"""
    def get_result(self):
        """Gets the result of the addition object"""
        return self.value_a + self.value_b
