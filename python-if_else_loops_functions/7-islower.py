#!/usr/bin/python3
def islower(c):
    comp = ord(c)
    for i in range(97, 123):
        if i == comp:
            return True
        else:
            return False
