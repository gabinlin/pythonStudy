#!/bin/bash/python3
inStr = input()
num = eval(inStr)
showStr = 'Hello World'
if num == 0:
    print(showStr)
elif num > 0:
    count = len(showStr)
    if 0 != count%2:
        count = count + 1
    for i in range(int(count/2)):
        end = (i+1)*2
        if end > len(showStr):
            end = len(showStr)
        print(showStr[i*2:end])

else:
    for i in range(len(showStr)):
        print(showStr[i])