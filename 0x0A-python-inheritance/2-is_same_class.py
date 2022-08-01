#!/usr/bin/python3
def is_same_class(obj, a_class):
    """function that returns True if the object is exactly an instance of the specified class
    Args:
        obj(any): The object to check
        a_class(type): The class for object to compare
    Returns:
        If object is exactly an instance of a_class - True
        Otherwise - False
    """
    if type(obj) == a_class:
        return True
    return False
