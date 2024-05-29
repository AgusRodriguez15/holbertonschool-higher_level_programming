#!/usr/bin/python3
"""script that adds all arguments to a Python list, then save them to a file"""
import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    lista = load_from_json_file(filename)
except FileNotFoundError:
    lista = []

for i in sys.argv[1:]:
    lista.append(i[0:])
save_to_json_file(lista, filename)
