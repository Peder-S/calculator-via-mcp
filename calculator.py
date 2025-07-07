#!/usr/bin/env python3
"""
Terminal-based calculator
"""

def main():
    print("Welcome to the terminal-based calculator!\n")
    print("Enter calculations in the format: <number> <operator> <number>")
    print("Supported operators: +, -, *, /")
    print("Type 'exit' or 'quit' to end the program.\n")

    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b if b != 0 else float('inf'),
    }

    while True:
        user_input = input('> ').strip()
        if not user_input:
            continue
        if user_input.lower() in ('exit', 'quit'):
            print('Goodbye!')
            break
        parts = user_input.split()
        if len(parts) != 3:
            print("Invalid format. Usage: <number> <operator> <number>")
            continue
        num1_str, op, num2_str = parts
        try:
            num1 = float(num1_str)
            num2 = float(num2_str)
        except ValueError:
            print("Invalid numbers. Please enter valid numeric values.")
            continue
        func = operations.get(op)
        if not func:
            print(f"Unsupported operator '{op}'. Supported operators: +, -, *, /")
            continue
        try:
            result = func(num1, num2)
        except Exception as e:
            print(f"Error during calculation: {e}")
            continue
        print(f"Result: {result}\n")

if __name__ == '__main__':
    main()
