"""
Core calculator operations
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def power(a, b):
    return a ** b

def modulo(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot modulo by zero")
    return a % b

OPERATIONS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '**': power,
    '^': power,
    '%': modulo,
}