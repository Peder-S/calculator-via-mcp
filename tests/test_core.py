import pytest
from calculator.core import add, subtract, multiply, divide, power, modulo

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(4, 2) == 8

def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)

def test_power():
    assert power(2, 3) == 8

def test_modulo():
    assert modulo(10, 3) == 1
    with pytest.raises(ZeroDivisionError):
        modulo(5, 0)
