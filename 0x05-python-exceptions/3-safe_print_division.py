#!/usr/bin/python3

def calculate_safe_division(a, b):
    """Calculates the division of a by b and returns the result.

    Args:
        a (numeric): The numerator.
        b (numeric): The denominator.

    Returns:
        The division result if it's valid, otherwise None.
    """
    try:
        division_result = a / b
    except (TypeError, ZeroDivisionError):
        division_result = None
    finally:
        print("Calculated result: {}".format(division_result))
    return (division_result)
