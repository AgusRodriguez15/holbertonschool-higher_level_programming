#!/usr/bin/python3
"""read the file"""


def read_file(filename=""):
    """read the file"""
    with open(filename, 'r', encoding="UTF-8") as f:
        print(f.read(), end='')
