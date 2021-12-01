"""Main function to initiate the calculator_test.py file"""

from time import sleep
import pytest


print('main.py will pytest for the calculator_test.py file')
sleep(3)


def main():
    """Runs the pytest program for the calculator"""
    print('Running pytest for calculator.py ...')
    retcode = pytest.main(['--pylint', 'calculator/tests/calculator_test.py'])
    print(retcode)
    print("Test complete")


if __name__ == '__main__':
    main()
