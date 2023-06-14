#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """Replace or add key/value pairs in a dictionary."""
    updated_dictionary = a_dictionary.copy()
    updated_dictionary[key] = value
    return updated_dictionary
