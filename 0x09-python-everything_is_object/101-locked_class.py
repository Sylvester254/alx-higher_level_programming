#!/usr/bin/python3
"""Defines LockedClass"""


class LockedClass():
    """
    Prevents the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name.
    """
    __slots__ = ["first_name"]

    def __init__(self):
        """Creates new instance of LockedClass."""
        self.first_name = "first_name"
