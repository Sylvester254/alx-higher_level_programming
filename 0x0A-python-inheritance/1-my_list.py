#!/usr/bin/python3
"""Defines class MyList that inherits from list"""


class MyList(list):
    """
    Args: mylist: list to sort in ascending order 
    """
    def print_sorted(self):
        """
        Public instance method that prints the sorted list
        """
        mylist = self[:]
        mylist.sort()
        print(mylist)
