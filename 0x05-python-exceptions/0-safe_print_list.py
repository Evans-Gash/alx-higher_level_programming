#!/usr/bin/python3

def print_elements(my_list=[], x=0):
    """Print a specified number of elements from a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements from my_list to print.

    Returns:
        The number of elements printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            break
    print("")
    return (count)
