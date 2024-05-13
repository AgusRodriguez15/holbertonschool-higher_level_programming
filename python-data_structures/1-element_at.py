#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    if idx > my_list:
        return None
    while idx == my_list:
        print("{}".format(my_list[idx]))
