#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    i = 2
    new = {key: value * i for key, value in a_dictionary.items()}
    return new
