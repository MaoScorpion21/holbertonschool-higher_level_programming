#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max = my_list[0]
        for one in my_list:
            if one > max:
                max = one
        return max
    return None
