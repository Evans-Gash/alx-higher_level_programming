#!/usr/bin/python3

def divide_lists_elementwise(list_1, list_2, length):
    """Divides two lists element by element.

    Args:
        list_1 (list): The first list.
        list_2 (list): The second list.
        length (int): The number of elements to divide.

    Returns:
        A new list of length 'length' containing the divisions.
    """
    result_list = []
    for i in range(length):
        try:
            division = list_1[i] / list_2[i]
        except TypeError:
            print("Invalid type encountered")
            division = 0
        except ZeroDivisionError:
            print("Division by zero error")
            division = 0
        except IndexError:
            print("Index out of range")
            division = 0
        finally:
            result_list.append(division)
    return (result_list)
