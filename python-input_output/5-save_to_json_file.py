#!/usr/bin/python3
"""returns the JSON"""
import json


def save_to_json_file(my_obj, filename):
    """returns the JSON"""
    with open(filename, 'w', encoding="UTF-8") as fileNew:
        json.dump(my_obj, fileNew)
