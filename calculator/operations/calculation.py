"""This is the calculation class / abstraction class"""


class Calculation:
    """Creates the Calculation parent class for the arithmetic subclasses"""
    # pylint: disable=bad-option-value, too-few-public-methods
    def __init__(self, values: tuple):
        """Constructor Method"""
        self.values = Calculation.convert_to_float(values)

    @classmethod
    def create(cls, values: tuple):
        """Creates an object"""
        return cls(values)

    @staticmethod
    def convert_to_float(values):
        """Converts the values passed to function into float values in a list"""
        list_of_floats = []
        for item in values:
            list_of_floats.append(float(item))
        return tuple(list_of_floats)
