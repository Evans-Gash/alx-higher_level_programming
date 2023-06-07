#!/usr/bin/python3
def print_tebahpla():
    """Print the alphabet in reverse order alternating CAPS & Small Letters."""
    i = 0
    for c in range(ord('z'), ord('a') - 1, -1):
        print("{}".format(chr(c - i)), end="")
        i = 32 if i == 0 else 0


# Call the function to print the tebahpla
print_tebahpla()
