#!/usr/bin/python3
"""script that adds all arguments to a Python list, and then save them to a file"""
import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

argvv = sys.argv
filename = "add_item.json"

with open(filename, 'a+', encoding="utf-8") as new_file:
    lista = []
    lista.append(argvv[1:])
    save_to_json_file(lista, filename) and load_from_json_file(filename)
    

