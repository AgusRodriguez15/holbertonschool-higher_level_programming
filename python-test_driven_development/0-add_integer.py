#!/usr/bin/python3

"holaaaa"


def add_integer(a, b=98):
    """
    Esta función suma dos números enteros o de punto flotante

    Args:
        a (int, float): El primer número a sumar.
        b (int, float, opcional): El segundo número a sumar. Por defecto es 98.

    Returns:
        int: La suma de los dos números, convertida a entero.

    Raises:
        TypeError: Si alguno de los argumentos no es un entero o un flotante.
    """
    # Comprobar si a y b son enteros o flotantes
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    # Convertir a y b a enteros y sumarlos
    return int(a) + int(b)
