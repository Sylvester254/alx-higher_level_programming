#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
class Rectangle that inherits from class BaseGeometry
"""

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """
        initializing a rectangle
        Args:
            width(int): width of rectangle
            height(int): height of rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
