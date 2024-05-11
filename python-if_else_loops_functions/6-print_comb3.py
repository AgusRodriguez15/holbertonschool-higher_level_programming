#!/usr/bin/python3
for i in range (10):
    for j in range (10):
        comb = str(i) + str(j)
        if str(i) != str(j):
            print("{}".format(comb), end=", ")
    else:
        print("{}".format(comb))
