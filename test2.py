#!/usr/bin/python3

kArray = input()

def str_array_turn_to_num_array(str_array):
    array_temp = str_array.split(" ")
    num_array = [0] * len(array_temp)
    j = 0
    for s in array_temp:
        num_array[j] = eval(s)
        j += 1
    return num_array

numArray = str_array_turn_to_num_array(kArray)

def calculate_max_sum(array):
    size = len(array)
    this_sum = 0
    max_sum = 0
    for i in range(size):
        t = array[i]
        this_sum += t
        if this_sum < 0:
            this_sum = 0
        else:
            if this_sum > max_sum:
                max_sum = this_sum
    return max_sum

print(calculate_max_sum(str_array_turn_to_num_array(kArray)))