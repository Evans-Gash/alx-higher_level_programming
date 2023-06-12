#!/usr/bin/python3


def replace_in_list(evans_list, idx, element):
    """Replace an element of a list at a specific position."""
    if idx >= 0 and idx < len(evans_list):
        evans_list[idx] = element
    return evans_list


if __name__ == "__main__":
    evans_list = [1, 2, 3, 4, 5]
    index = 2
    new_element = 7
    result = replace_in_list(evans_list, index, new_element)
    print(result)
