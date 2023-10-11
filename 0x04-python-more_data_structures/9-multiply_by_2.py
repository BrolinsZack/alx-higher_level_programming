#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for d, x in a_dictionary.items():
        new_dict[d] = 2 * x
    return new_dict
