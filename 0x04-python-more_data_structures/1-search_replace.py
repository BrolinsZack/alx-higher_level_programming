#!/usr/bin/python3


def search_replace(my_list, search, replace):
    if my_list is None:
        return
    new_list = my_list[:]
    for idx, j in enumerate(new_list):
        if j == search:
            new_list[idx] = replace
    return new_list
