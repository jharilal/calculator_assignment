"""Holds the history class and history operations for the calculator"""


class History:
    """Holds the methods for history operations on the calculator"""
    history = []

    @staticmethod
    def append_to_history(result):
        """Adds a calculation object to the history"""
        History.history.append(result)
        return True

    @staticmethod
    def last_result():
        """Returns the most recent result of the calculator history"""
        return History.history[-1].get_result()

    @staticmethod
    def get_last_object():
        """Returns the most recent object of the calculator history"""
        return History.history[-1]

    @staticmethod
    def first_result():
        """Returns the first result of the calculator history"""
        return History.history[0].get_result()

    @staticmethod
    def get_first_object():
        """Returns the first object of the calculator history"""
        return History.history[0]

    @staticmethod
    def history_count():
        """Returns the total number of calculation objects in the history"""
        return len(History.history)

    @staticmethod
    def get_history():
        """Returns a list of calculation objects"""
        return History.history

    @staticmethod
    def clear_history():
        """Removes all calculations from the calculation history"""
        History.history = []
        return True
