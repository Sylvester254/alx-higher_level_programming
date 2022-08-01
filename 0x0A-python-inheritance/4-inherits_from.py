#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    function that checks if the object is
    an instance of a class that inherited
    (directly or indirectly) from the specified class.
    Args:
        obj(any): The object to check
        a_class(type): The class for object to compare
    Returns:
        If object is exactly an instance of a_class - True
        Otherwise - False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
