#!/usr/bin/python3


def no_c(my_string):
    """Remove all characters c and C from a string."""
    filtered_chars = [char for char in my_string if char.lower() != 'c']
    return ''.join(filtered_chars)


if __name__ == "__main__":
    input_string = "Yooow! This is a test string."
    result = no_c(input_string)
    print(result)
