#!/usr/bin/python3
from itertools import count


if __name__ == "__main__":
    import sys

    from calculator_1 import add, sub, mul, div
    
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    count = len(sys.argv) - 1
    if count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
        sys.exit(1)
    ops = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in list(ops.keys()):
        print("Unknown operator. Available operators: +, -, * and /\n")
        sys.exit(1)
    print(f"{a} {sys.argv[2]} {b} = {ops[sys.argv[2]](a, b)}")
