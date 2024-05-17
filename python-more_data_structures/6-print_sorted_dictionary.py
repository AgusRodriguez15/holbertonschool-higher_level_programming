#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keyss = sorted(a_dictionary.keys())
    for key in keyss:
        print(f"{key}: {a_dictionary[key]}")
