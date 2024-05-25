#!/usr/bin/python3

"""
more clases
"""


class Rectangle:  # Clase Rectangle
    """
    clases
    """
    def __init__(self, width=0, height=0):
        """def init """
        self.height = height
        self.width = width

    @property
    def width(self):
        """retrieve it"""
        return self.__width

    @width.setter
    def width(self, value):
        """set it"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieve it"""
        return self.__height

    @height.setter
    def height(self, value):
        """set it"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculate the area of the rectangle"""
        area = self.__height * self.width
        return area

    def perimeter(self):
        """calculate the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 
        permiter = self.__height + self.__width + self.__width + self.__height
        return permiter
