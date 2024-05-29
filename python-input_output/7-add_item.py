#!/usr/bin/python3
"""script that adds all arguments to a Python list, then save them to a file"""
import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
filenamee = "add_item.json"

load_from_json_file(filenamee)
arguments = sys.argv
with open(filenamee, 'a+', encoding="utf-8") as new_file:
    lista = []
    for argv in arguments:
        lista.append(argv[0:])
    save_to_json_file(lista, filenamee)
    load_from_json_file(filenamee)
