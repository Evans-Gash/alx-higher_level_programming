#!/usr/bin/python3


def element_at(evans_list, idx):
    """Retrieve an element from a list."""
    if idx < 0 or idx >= len(evans_list):
        return None
    return evans_list[idx]


if __name__ == "__main__":
    gash_list = [1, 2, 3, 4, 5]
    index = 2
    result = element_at(gash_list, index)
    print(result)
