#!/usr/bin/python3
"""Defines class BaseGeometry"""


class BaseGeometry:
    def area(self):
        """
        Area function.
        Raises:
            Exception: if area is not implemented.
        """
        self.msg = "area() is not implemented"
        raise Exception(self.msg)
