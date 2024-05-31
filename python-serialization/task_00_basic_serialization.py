#!/usr/bin/python3

from json import dump, load


"""basic serialization module that adds"""


def serialize_and_save_to_file(data, filename):
    """serialize"""
    with open(filename, 'w', encoding="UTF-8") as fileNew:
        dump(data, fileNew)


def load_and_deserialize(filename):
    """Load and deserialize"""
    with open(filename, 'r', encoding="utf-8") as filenew:
        return load(filenew)
