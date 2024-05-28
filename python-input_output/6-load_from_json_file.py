#!/usr/bin/python3
"""returns the JSON"""
import json


def load_from_json_file(filename):
    """returns the JSON"""
    with open(filename, 'w', encoding="UTF-8") as fil:
        x = json.load(fil)
    return x 
