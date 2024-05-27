#!/usr/bin/python3
"""add a string to the final"""


def append_write(filename="", text=""):
    """add a string to the final"""
    with open(filename, 'a', encoding="UTF-8") as f:
        return f.write(text)
