#!/usr/bin/python3
"""Defines an object attribute lookup function"""


def lookup(obj):
    """
    function that returns list of available attributes
     and methods of an object
    """
    list = dir(obj)
    return list
