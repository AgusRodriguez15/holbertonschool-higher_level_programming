#!/usr/bin/python3
"""add a string to the final"""


def append_write(filename="", text=""):
    """add a string to the final"""
    with open(filename, 'w', encoding="UTF-8") as f:
        f.write(text)
        return len(text)
