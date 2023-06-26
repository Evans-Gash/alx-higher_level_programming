#!/usr/bin/python3

import sys


def execute_function_safely(func, *args):
    """Executes a function safely.

    Args:
        func: The function to execute.
        args: Arguments for the function.

    Returns:
        If an error occurs - None.
        Otherwise - the result of the function call.
    """
    try:
        result = func(*args)
        return (result)
    except Exception as e:
        print("Error: {}".format(e), file=sys.stderr)
        return (None)
