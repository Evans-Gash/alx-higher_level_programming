#!/usr/bin/python3

import sys

if __name__ == "__main__":
    arguments = sys.argv[1:]  # Exclude the script name from the arguments list

    # Convert arguments to integers and calculate the sum
    total = sum(int(arg) for arg in arguments)

    print(total)
