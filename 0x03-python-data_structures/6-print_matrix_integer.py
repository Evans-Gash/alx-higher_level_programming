#!/usr/bin/python3

def print_matrix_integer(matrix=None):
    if matrix is None:
        return

    for row in matrix:
        for i, col in enumerate(row):
            print("{:d}".format(col), end=" " if i != len(row) - 1 else "")
        print()


if __name__ == "__main__":
    the_one_the_only_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print_matrix_integer(the_one_the_only_matrix)
