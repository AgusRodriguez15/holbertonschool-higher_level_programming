#!/usr/bin/python3
import pickle

"""task_01_pickle"""


class CustomObject:

    """create class"""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Is Student:", self.is_student)

    def serialize(self, filename):
        with open(filename, 'wb') as fileNew:
            pickle.dump(self, fileNew)

    @classmethod
    def deserialize(cls, filename):
        with open(filename, 'rb') as file:
            obj = pickle.load(file)
        return obj
