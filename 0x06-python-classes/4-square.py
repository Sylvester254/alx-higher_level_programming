#!/usr/bin/python3
#!/usr/bin/python3
"""Defines class Square"""

class Square:
    """
    class Square that defines a square by: (based on 1-square.py)

    Attributes:
        size: size of a square 
    """
    def __init__(self, size=0):
        """creates new instance of square
        
        args:
            size: size of the square.
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    
    def area(self):
        """Calculates the area of square
        
        Returns: the current square area.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Returns the size of a square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter for size.
        Args:
            value (int): size of a square (1 side).
        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
