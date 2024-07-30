#!/usr/bin/env python3

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    def perimeter(self):
        pass
    
class Circle(Shape):
    
    def __init__(self, radius=0):
        """def init """
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return math.pi * self.radius * 2
    
class Rectangle(Shape):
    
    def __init__(self, width=0, height=0):
        """def init """
        self.height = height
        self.width = width
        
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return self.width + self.height + self.width + self.height
    
def shape_info(shape):
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())