#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div = (a / b)
    except (ZeroDivisionError,TypeError):
        return(None)
    finally:
        print("Inside results: {:d}".format(div))
        return(div)
