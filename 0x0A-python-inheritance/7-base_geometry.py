#!/usr/bin/python3
"""Defines class BaseGeometry based on 6-base_geometry"""


class BaseGeometry:
    def area(self):
        """
        Area function.
        Raises:
            Exception: if area is not implemented.
        """
        self.msg = "area() is not implemented"
        raise Exception(self.msg)
    def integer_validator(self, name, value):
        """
        Instance method that validates value
        Args:
            name(str): object's name
            value(int): object's property
        Raises:
            TypeError: if value is not an int.
            ValueError: if value is less or equal to 0.
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
