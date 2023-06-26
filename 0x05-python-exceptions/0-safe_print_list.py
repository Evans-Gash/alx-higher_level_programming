#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print Specified elememts of a list.

    Args:
        my_list (list): Actual List to get the elements
        x (int): Elements to be printed

    Returns:
        The number of elements printed.
    """
    gash = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            gash += 1
        except IndexError:
            break
    print("")
    return (gash)
