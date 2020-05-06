timeStr = input()
unit = timeStr[-1]
if unit in ['F', 'f']:
    print('{:.2f}C'.format((eval(timeStr[0:-1])-32)/1.8))
elif unit in ['C', 'c']:
    print('{:.2f}F'.format(eval(timeStr[0:-1])*1.8+32))
else:
    print('输入格式错误')