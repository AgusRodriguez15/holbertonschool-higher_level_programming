#!/usr/bin/python3
"""create an empty class"""


class BaseGeometry:
    """class"""
    def area(self):
        """use exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
