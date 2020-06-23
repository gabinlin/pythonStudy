#!/usr/bin/python3
# 在线算法
k = input()
kArray = input()

def caculateMaxSum(array, k):
    maxSum = 0;
    thisSum = 0
    for i in range(k):
        n = eval(array[i])
        thisSum += n
        if thisSum < 0: thisSum = 0
        elif thisSum > maxSum: maxSum = thisSum
    return maxSum

print(caculateMaxSum(kArray.split(" "), eval(k)))