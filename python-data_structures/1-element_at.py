#!/usr/bin/python3
def element_at(my_list, idx):
    for i in my_list:
        int(i)
    if idx < 0:
        return None
    if idx > i:
        return None
    while idx == i:
        print("{:d}".format(my_list[idx]))
