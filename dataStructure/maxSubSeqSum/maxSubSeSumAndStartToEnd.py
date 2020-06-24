#!/usr/bin/python3
# 计算最大子列和，以及子列和的起始点
sizeInput = eval(input())
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

def calculate_max_sum(array, size):
    this_sum = 0
    max_sum = 0

    this_start = -1
    final_start = 0
    final_end = size - 1
    for i in range(size):
        t = array[i]
        this_sum += t
        if this_sum < 0:
            this_sum = 0
            # 前段计算被丢弃后，重置this_start
            this_start = -1
        else:
            # 第一次初始化，this_start
            if this_start < 0: this_start = i
            if this_sum > max_sum or (this_sum == max_sum and this_start == i):
                max_sum = this_sum
                final_start = this_start
                final_end = i
    return [max_sum, array[final_start], array[final_end]]

result = calculate_max_sum(str_array_turn_to_num_array(kArray), sizeInput)
print(result[0], result[1], result[2], end="")