#!/usr/bin/python3
"""inherits from"""


def inherits_from(obj, a_class):
    """inherited"""
    return isinstance(obj, a_class) and type(obj) is not a_class
