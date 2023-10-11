#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = []
    for row in matrix:
        new_row = sq_list(row)
        new_list.append(new_row)
    return new_list


def sq_list(a):
    return [x**2 for x in y] 
