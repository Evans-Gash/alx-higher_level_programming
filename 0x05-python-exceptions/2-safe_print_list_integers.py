#!/usr/bin/python3

def print_integer_elements(gash_list=[], x=0):
    """Print the first x integer elements from a list.

    Args:
        gash_list (list): The list to print elements from.
        x (int): The number of integer elements from gash_list to print.

    Returns:
        The number of integer elements printed.
    """
    count = 0
    for element in gash_list[:x]:
        if isinstance(element, int):
            print(str(element), end="")
            count += 1
    print("")
    return (count)
