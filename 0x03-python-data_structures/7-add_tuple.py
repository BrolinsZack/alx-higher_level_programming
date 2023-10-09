#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    new_tuple = ()

    First tuple = tuple a + (0, 0)
    Second tuple = tuple b + (0, 0)
    new_tuple = First tuple[0] + Second tuple[0], First tuple[1] + Second tuple[1]
    return new_tuple
