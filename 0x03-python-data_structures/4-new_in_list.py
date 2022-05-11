#!/usr/bin/python3
def element_at(my_list, idx):
    magic_counter = len(my_list)
    if idx < 0 or idx > magic_counter - 1:
        return "None"
    Index = my_list[idx]
    return Index
