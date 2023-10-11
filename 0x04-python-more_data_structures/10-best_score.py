#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_v = max(list(a_dictionary.values()))
    for i, v in a_dictionary.items():
        if v == max_v:
            return i
    return None
