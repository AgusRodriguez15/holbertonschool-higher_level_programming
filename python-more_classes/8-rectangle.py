#!/usr/bin/python3

"""
more clases
"""


class Rectangle:  # Clase Rectangle
    """
    clases
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """def init """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
        return str(area)

    def perimeter(self):
        """calculate the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return "0"
        permiter = self.__height + self.__width + self.__width + self.__height
        return str(permiter)

    def print_rectangle(self):
        """create the rectangle"""
        height = self.__height
        width = self.__width
        if height == 0 or width == 0:
            return ""
        a = '\n'.join(Rectangle.print_symbol * width for i in range(height))
        return a

    def __str__(self):
        """print the rectangle"""
        return f"{self.print_rectangle()}"

    def __repr__(self):
        """print the rectangle like a string"""
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        """print a message when an instanced is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_rect_1 = rect_1.width * rect_1.height
        area_rect_2 = rect_2.width * rect_2.height

        if area_rect_1 >= area_rect_2:
            return rect_1
        else:
            return rect_2
