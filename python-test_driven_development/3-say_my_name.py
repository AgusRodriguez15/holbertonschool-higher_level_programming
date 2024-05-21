#!/usr/bin/python3

""""3 solution"""

def say_my_name(first_name, last_name=""):             
    """
    Imprime el nombre completo con el formato "My name is <first_name> <last_name>$".

    Parámetros:
    first_name (str): El primer nombre.
    last_name (str, opcional): El apellido. Por defecto es una cadena vacía.

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    print("My name is {} {}".format(first_name, last_name))