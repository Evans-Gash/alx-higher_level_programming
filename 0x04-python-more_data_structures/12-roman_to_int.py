#!/usr/bin/python3

def to_subtract(list_num):
    subtracted_value = 0
    max_list = max(list_num)

    for n in list_num:
        if max_list > n:
            subtracted_value += n

    return max_list - subtracted_value


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_keys = list(rom_nums.keys())

    num = 0
    last_rom = 0
    list_num = [0]

    for ch in roman_string:
        for r_num in roman_keys:
            if r_num == ch:
                if rom_nums.get(ch) <= last_rom:
                    num += to_subtract(list_num)
                    list_num = [rom_nums.get(ch)]
                else:
                    list_num.append(rom_nums.get(ch))

                last_rom = rom_nums.get(ch)

    num += to_subtract(list_num)

    return num
