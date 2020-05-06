#!/bin/bash/python3
# 温度转换

timeStr=input('请输入待转化的温度值(带C或F符号)')
unit=timeStr[-1]
if unit in ['F', 'f']:
    print('转化后的温度{:.2f}C'.format((eval(timeStr[0:-1])-32)/1.8))
elif unit in ['C', 'c']:
    print('转化后的温度{:.2f}F'.format(eval(timeStr[0:-1])*1.8+32))
else:
    print('输入格式错误')