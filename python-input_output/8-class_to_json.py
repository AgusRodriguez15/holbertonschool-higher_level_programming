#!/usr/bin/python3
"""script that adds all arguments to a Python list, then save them to a file"""
def class_to_json(obj):
    dictionary = {}
    dictionary = obj.__dict__
    return dictionary   
