#!/usr/bin/python3


def max_integer(evans_list=None):
    """Find the biggest integer of a list."""
    if evans_list is None or len(evans_list) == 0:
        return None

    gigantic = evans_list[0]
    for i in range(1, len(evans_list)):
        if evans_list[i] > gigantic:
            gigantic = evans_list[i]

    return gigantic


if __name__ == "__main__":
    gash_list = [4, 2, 9, 5, 1]
    result = max_integer(gash_list)
    print(result)
