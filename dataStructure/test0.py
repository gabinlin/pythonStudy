import datetime

def f1(x, i):
    sum = 0
    for j in reversed(range(1, i + 1)):
        sum = x * (1 / j + sum)
    return sum + 1

def f2(x, i):
    sum = 0
    for j in range(1, i + 1):
        sum += x ** j / j
    return sum + 1

i = eval(input('1+x+x^2/2+x^3/3+……+x^i/i,请输入i，计算多项式的值'))
x = 1.1

k = 1000
start = datetime.datetime.now()
for y in range(k):
    f1(x, i)
print(datetime.datetime.now() - start)

start = datetime.datetime.now()
for y in range(k):
    f2(x, i)
print(datetime.datetime.now() - start)