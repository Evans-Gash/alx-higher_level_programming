#!/usr/bin/python3

def delete_at(evans_list=[], idx=0):
    """Delete an item at a specific position in a list."""
    if idx >= 0 and idx < len(evans_list):
        del evans_list[idx]
    return evans_list
