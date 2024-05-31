#!/usr/bin/python3
import json
"""basic serialization module that adds the functionality to serialize and deserialize the JSON file """


def serialize_and_save_to_file(filename, data):
    """serialize"""
    json.dump(filename, data)
    
def load_and_deserialize(filename):
    """Load and deserialize"""
    json.load(filename)
