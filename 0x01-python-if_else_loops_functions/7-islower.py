#!/usr/bin/python3


def islower(c):
    """scan for small letters."""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
