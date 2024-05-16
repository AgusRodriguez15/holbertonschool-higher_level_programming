#!/usr/bin/python3
def uniq_add(my_list=[]):
    b = []
    for i in my_list:
        if i not in b:
            b.append(i)
    return sum(b)
