money = input()
unit = money[0, 3]
value = money[3:]
print(unit)
if unit in ['rmb', 'RMB']:
    print('USD{:.2f}'.format(eval(value) * 6.78))
elif unit in ['usd', 'USD']:
    print('RMB{:.2f}'.format(eval(value) / 6.78))
else:
    pass