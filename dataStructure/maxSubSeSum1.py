#!/usr/bin/python3
# 最傻的算法1
k = input()
kArray = input()

def caculateMaxSum(array, k):
    maxSum = 0
    for i in range(k):
        for j in range(i, k):
            thisSum = 0
            for h in range(i, j):
              thisSum += eval(array[--h])
              if (thisSum > maxSum): maxSum = thisSum
    return maxSum

print(caculateMaxSum(kArray.split(" "), eval(k)))