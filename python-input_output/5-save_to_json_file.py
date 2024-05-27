#!/usr/bin/python3
"""returns the JSON"""
import json


def save_to_json_file(my_obj, filename):
    with open(filename, 'w', encoding="UTF-8") as f:
        return json.dumps(my_obj)
