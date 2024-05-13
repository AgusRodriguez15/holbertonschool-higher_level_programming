#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        comb = str(i) + str(j)
        if comb != '89':
            print("{}".format(comb), end=", ")
else:
    print("{}".format(comb))
