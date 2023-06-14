#!/usr/bin/python3

def search_replace(my_list, search, replace):
    latest_listde = [replace if x == search else x for x in my_list]
    return latest_listde
