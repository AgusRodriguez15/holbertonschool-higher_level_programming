#!/usr/bin/python3
"""create an empty class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
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

    def __init__(self, width, height):
        """inicialitate private"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self._width = width
        self._height = height
