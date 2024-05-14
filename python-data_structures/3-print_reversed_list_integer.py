#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    lon = len(my_list)
    for i in range(lon):
        print(my_list[lon-i-1])
