#!/usr/bin/python3
for a in range(9):
    for k in range(a + 1, 10):
        if a * 10 + k < 89:
            print("{:d}{:d}".format(a, k), end=", ")
print("{:d}".format(89))
