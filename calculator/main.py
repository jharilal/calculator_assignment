"""Creating a calculator"""


class Calculator:
    """Initiates a calculator that stores a value"""

    value = 0

    def adding(self, value_a):
        """Adds a value to the calculator"""
        self.value = self.value + value_a
        return self.value

    def subtracting(self, value_a):
        """Subtracts a value to the calculator"""
        self.value = self.value - value_a
        return self.value

    def multiplying(self, value_a):
        """Multiplies a value to the calculator"""
        self.value = self.value * value_a
        return self.value

    def dividing(self, value_a):
        """Divides a value against the calculator"""
        if value_a == 0:
            return ZeroDivisionError
        self.value = self.value / value_a
        return self.value
