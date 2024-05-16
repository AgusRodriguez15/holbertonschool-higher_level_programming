#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [val if val != search else replace for val in my_list]
    return new_list
