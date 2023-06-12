#!/usr/bin/python3


def replace_in_list(evans_list, idx, element):
    """Replace an element of a list at a specific position."""
    if idx >= 0 and idx < len(evans_list):
        new_list = evans_list.copy()
        new_list[idx] = element
        return new_list
    else:
        return evans_list


if __name__ == "__main__":
    gash_list = [1, 2, 3, 4, 5]
    index = 2
    new_element = 7
    result = replace_in_list(gash_list, index, new_element)
    print(result)
