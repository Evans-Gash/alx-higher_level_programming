#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    matrix_two_point_0 = [list(map(lambda x: x**2, row)) for row in matrix]

    return matrix_two_point_0
