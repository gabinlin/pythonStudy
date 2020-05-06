#!/bin/bash/python3
# -*- coding: UTF-8 -*-

# C=(F-32)/1.8
# F=C*1.8+32


def temp_covert():
    temp_str = input('请输入带有符号的温度，例如32C或100F:\n')
    prefix = temp_str[-1]
    if prefix in ['F', 'f']:
        C = (eval(temp_str[0:-1]) - 32) / 1.8
        print('转换后的温度是{:.2f}C'.format(C))
    elif prefix in ['C', 'c']:
        F = (eval(temp_str[0:-1]) * 1.8 + 32)
        print('转换后的温度是{:.2f}F'.format(F))
    else:
        print('输入格式错误')
    return ''


while True:
    temp_covert()
