#!/usr/bin/python3
"""read the file"""

def write_file(filename="", text=""):
    """add a string"""
    with open(filename, 'w', encoding="UTF-8") as f:
        f.write(text)
        