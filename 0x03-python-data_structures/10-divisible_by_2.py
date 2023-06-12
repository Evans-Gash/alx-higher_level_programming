#!/usr/bin/python3

def divisible_by_2(gash_list=None):
    """Find all multiples of 2 in a list."""
    if gash_list is None:
        return []

    multiples = []
    for i in range(len(gash_list)):
        if gash_list[i] % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)

    return multiples


if __name__ == "__main__":
    gash_list = [1, 2, 3, 4, 5, 6]
    result = divisible_by_2(gash_list)
    print(result)
