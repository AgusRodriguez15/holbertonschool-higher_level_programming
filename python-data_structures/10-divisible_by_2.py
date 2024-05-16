#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new = my_list.copy()
    for i in new:
        if new[i] % 2 == 0:
            return new, True
        else:
            return new, False
