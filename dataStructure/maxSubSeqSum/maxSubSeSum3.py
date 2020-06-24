#!/usr/bin/python3
kArray = input()

def caculateMaxSum(array):
    if len(array) == 1:
        temp = eval(array[0])
        if temp > 0: return temp
        else: return 0

    center = int(len(array) / 2)
    leftArray = array[0:center]
    maxLeftSum = caculateMaxSum(leftArray)
    rightArray = array[center:len(array)]
    maxRightSum = caculateMaxSum(rightArray)
    maxLeftSumTemp = 0
    leftSumTemp = 0
    leftArray.reverse()
    for left in leftArray:
        leftSumTemp += eval(left)
        if leftSumTemp > maxLeftSumTemp: maxLeftSumTemp = leftSumTemp

    maxRightSumTemp = 0
    rightSumTemp = 0
    for right in rightArray:
        rightSumTemp += eval(right)
        if rightSumTemp > maxRightSumTemp: maxRightSumTemp = rightSumTemp
    return max(maxLeftSum, maxRightSum, maxRightSumTemp + maxLeftSumTemp)

print(caculateMaxSum(kArray.split(" ")))