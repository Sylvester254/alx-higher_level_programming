#!/usr/bin/python3
"""defines a functiom to check instance of object"""


def is_kind_of_class(obj, a_class):
    """function that checks if the object is an
    instance of, or if the object is an instance of
    a class that inherited from, the specified class.
    Args:
        obj(any): The object to check
        a_class(type): The class for object to compare
    Returns:
        If object is exactly an instance of a_class - True
        Otherwise - False
    """
    if isinstance(obj, a_class):
        return True
    return False
