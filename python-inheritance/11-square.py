#!/usr/bin/python3}

"""create an empty class"""

BaseGeometry = __import__('9-rectangle').Rectangle


class Square(BaseGeometry):
    """class"""
    def area(self):
        """use exception"""
        return self._size * self._size

    def __init__(self, size):
        """inicialitate private"""
        self.integer_validator("size", size)
        self._size = size

    def __str__(self):
        return f"[Square] {self._size}/{self._size}"
