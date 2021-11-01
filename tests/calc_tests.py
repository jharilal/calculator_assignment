from calculator.calc_body import Calculator


def test_adding():
    """Tests the adding function of the calculator class"""
    test_calc = Calculator()
    assert test_calc.adding(6) == 6


def test_subtracting():
    """Tests the subtracting function of the calculator class"""
    test_calc = Calculator()
    assert test_calc.subtracting(2) == -2


def test_multiplying():
    """Tests the multiplying function of the calculator class"""
    test_calc = Calculator()
    test_calc.adding(2)
    assert test_calc.multiplying(4) == 8


def test_dividing():
    """Tests the dividing function of the calculator class"""
    test_calc = Calculator()
    test_calc.adding(10)
    assert test_calc.dividing(2) == 5


def test_dividing_zero():
    """Tests the diving function of the calculator class when dividing by 0"""
    test_calc = Calculator()
    test_calc.adding(1)
    assert test_calc.dividing(0) == ZeroDivisionError
