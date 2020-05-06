timeStr = input()
unit = timeStr[0]
if unit in ['F', 'f']:
    print('C{:.2f}'.format((eval(timeStr[1:len(timeStr)])-32)/1.8))
elif unit in ['C', 'c']:
    print('F{:.2f}'.format(eval(timeStr[1:len(timeStr)])*1.8+32))
else:
    print('输入格式错误')