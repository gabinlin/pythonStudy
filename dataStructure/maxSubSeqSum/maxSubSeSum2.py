#!/usr/bin/python3
k = input()
kArray = input()

def caculateMaxSum(array, k):
    maxSum = 0
    for i in range(k):
        --i
        thisSum = 0
        for j in range(i, k):
            --j
            thisSum += eval(array[j])
            if (thisSum > maxSum): maxSum = thisSum
    return maxSum

print(caculateMaxSum(kArray.split(" "), eval(k)))