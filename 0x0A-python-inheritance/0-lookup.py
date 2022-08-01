#!/usr/bin/python3
def lookup(obj):
    """
    function that returns list of available attributes
     and methods of an object
    """
    list = dir(obj)
    return list
