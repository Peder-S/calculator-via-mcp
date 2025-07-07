"""
Command-line interface for the calculator
"""

import argparse
import sys
from .core import OPERATIONS

def evaluate_expression(expr):
    parts = expr.strip().split()
    if len(parts) != 3:
        raise ValueError("Expression must be in the format: <number> <operator> <number>")
    num1_str, op, num2_str = parts
    try:
        num1 = float(num1_str)
        num2 = float(num2_str)
    except ValueError:
        raise ValueError("Invalid numbers. Please enter numeric values.")
    func = OPERATIONS.get(op)
    if not func:
        raise ValueError(f"Unsupported operator '{op}'. Supported: {', '.join(OPERATIONS.keys())}")
    return func(num1, num2)

def main():
    parser = argparse.ArgumentParser(description="Terminal-based calculator")
    parser.add_argument('expression', nargs='*', help="Calculation expression: <number> <operator> <number>")
    args = parser.parse_args()

    if args.expression:
        expr = ' '.join(args.expression)
        try:
            result = evaluate_expression(expr)
            print(result)
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print("Welcome to the interactive calculator!\n")
        print("Enter calculations in the format: <number> <operator> <number>")
        print("Supported operators: " + ', '.join(OPERATIONS.keys()))
        print("Type 'exit' or 'quit' to end.\n")
        while True:
            inp = input('> ').strip()
            if not inp:
                continue
            if inp.lower() in ('exit', 'quit'):
                print("Goodbye!")
                break
            try:
                result = evaluate_expression(inp)
                print(result)
            except Exception as e:
                print(f"Error: {e}")

if __name__ == '__main__':
    main()