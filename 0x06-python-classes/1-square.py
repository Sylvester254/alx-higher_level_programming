#!/usr/bin/python3
"""Defines class Square"""


class Square:
    """
    class Square that defines a square by: (based on 0-square.py)

    Attributes:
        size: size of a square
    """
    def __init__(self, size):
        """creates new instance of square

        args:
            size: size of the square.
        """
        self.__size = size
