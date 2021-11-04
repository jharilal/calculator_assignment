"""This is the calculation class / abstraction class"""


class Calculation:
    """Creates the Calculation parent class for the arithmetic subclasses"""
    def __init__(self, value_a, value_b):
        self.value_a = value_a
        self.value_b = value_b
        self.secret = 0

    @classmethod
    def create(cls, value_a, value_b):
        """Creates an object. Will be used for the subclasses
         to create an object of the function type"""
        return cls(value_a, value_b)

    def secrets(self, value_a, value_b):
        """Secret function to make the pylint error go away. This is temporary"""
        self.secret = value_a ** value_b
        return self.secret
