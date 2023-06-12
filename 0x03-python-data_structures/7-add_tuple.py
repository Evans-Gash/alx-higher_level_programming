#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """Add two tuples."""
    def validate_tuple(tuple):
        if len(tuple) < 2:
            if len(tuple) == 0:
                return 0, 0
            else:
                return tuple[0], 0
        return tuple

    tuple_a = validate_tuple(tuple_a)
    tuple_b = validate_tuple(tuple_b)

    return tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]


if __name__ == "__main__":
    tuple_1 = (1, 2)
    tuple_2 = (3, 4)
    result = add_tuple(tuple_1, tuple_2)
    print(result)
