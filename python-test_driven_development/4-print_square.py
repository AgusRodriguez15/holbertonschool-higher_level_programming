#!/usr/bin/python3


"""4 print square"""


def print_square(size):

    """
    Imprime un cuadrado de tamaño `size` utilizando el carácter '#'

    Parámetros:
    size (int): El tamaño del lado del cuadrado.

    Excepciones:
    TypeError: Se levanta si `size` no es un entero.
    ValueError: Se levanta si `size` es menor que 0.
    """

    if not isinstance(size, (int)):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
