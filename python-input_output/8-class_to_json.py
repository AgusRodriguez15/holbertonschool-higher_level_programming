#!/usr/bin/python3
"""script that adds all arguments to a Python list, then save them to a file"""
import json
def class_to_json(obj):
    dictionary = {}

    # Pasar todos los atributos del objeto a un diccionario
    # "inspeccionar" obj y poner todo lo que tiene adentro de dictionary
    #print(vars(obj))
    dictionary = obj.__dict__
    


    return dictionary   
