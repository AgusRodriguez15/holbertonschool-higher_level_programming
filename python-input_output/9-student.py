#!/usr/bin/python3
"""
squareeeee
"""


class Student:
    def __init__(self, first_name, last_name, age):

        self.first_name = first_name
        self.lastname = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
