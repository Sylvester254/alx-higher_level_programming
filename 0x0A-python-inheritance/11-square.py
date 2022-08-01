#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""Defines a Rectangle subclass Square."""


class Square(Rectangle):
    def __init__(self, size):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
