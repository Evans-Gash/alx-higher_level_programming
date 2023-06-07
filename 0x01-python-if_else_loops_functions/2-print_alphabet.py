#!/usr/bin/python3
"""Print the alphabets in small letters, there shouldn't be a new line after."""
def print_alphabet():
    for letter in range(97, 123):
        print("{}".format(chr(letter)), end="")

if __name__ == "__main__":
    print_alphabet()
