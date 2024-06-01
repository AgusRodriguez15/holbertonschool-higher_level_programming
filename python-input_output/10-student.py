#!/usr/bin/python3
"""
squareeeee
"""


class Student:
    def __init__(self, first_name, last_name, age):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        if type(attrs) is list:
            dicc = {}
            for key in attrs:
                if key == 'first_name':
                    dicc[key] = self.first_name
                if key == 'last_name':
                    dicc[key] = self.last_name
                if key == 'age':
                    dicc[key] = self.age
            return dicc
