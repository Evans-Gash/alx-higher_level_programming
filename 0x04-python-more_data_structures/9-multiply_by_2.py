#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    multiplied_dictionary = a_dictionary.copy()
    dictionary_keys = list(multiplied_dictionary.keys())

    for key in dictionary_keys:
        multiplied_dictionary[key] *= 2

    return multiplied_dictionary
