#!/usr/bin/python3


def new_in_list(gash_list, idx, element):
    """Replace an element in a copied list at a specific position."""
    if idx < 0 or idx >= len(gash_list):
        return gash_list

    copy = gash_list.copy()
    copy[idx] = element
    return copy


if __name__ == "__main__":
    gash_list = [1, 2, 3, 4, 5]
    index = 2
    new_element = 7
    result = new_in_list(gash_list, index, new_element)
    print(result)
