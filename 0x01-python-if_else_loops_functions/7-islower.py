#!/usr/bin/python3def islower(c):

"""scan for small letters."""

def is_lowercase(c):
    return 97 <= ord(c) <= 122

if __name__ == "__main__":
    c = input("Enter a character: ")
    print(is_lowercase(c))    