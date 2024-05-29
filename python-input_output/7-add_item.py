#!/usr/bin/python3
"""script that adds all arguments to a Python list, then save them to a file"""
import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

argvv = sys.argv
filename = "add_item.json"

with open(filename, 'a+', encoding="utf-8") as new_file:
    lista = []
    for i in argvv[1:]:
        lista.append(i[0:])
    new_list = lista.copy()
    save_to_json_file(new_list, filename)
    new_list = load_from_json_file(filename)
