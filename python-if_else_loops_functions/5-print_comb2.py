#!/usr/bin/python3
for numbers in range(00, 100):
    add_zero = str(numbers).zfill(2)
    if numbers != 99:
        print ("{}".format(add_zero), end=", ")
    else:
        print("{}".format(add_zero))
        