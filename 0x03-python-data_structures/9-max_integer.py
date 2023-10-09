#!/usr/bin/python3
def max_integer(my_list=[]):
    
    a = len(my_list)
    if a < 1:
        return None
    else:
        max = my_list[0]
        for j in range(1, a):
            if my_list[j] > max:
                max = my_list[j]

        return max
