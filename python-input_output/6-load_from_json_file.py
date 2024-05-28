#!/usr/bin/python3
"""returns the JSON"""
import json


def load_from_json_file(filename):
    """returns the JSON"""
    with open(filename, encoding="UTF-8") as fil:
        return json.load(fil)
