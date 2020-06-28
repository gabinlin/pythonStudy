i = eval(input('1+x+x^2/2+x^3/3+……+x^i/i,请输入i，计算多项式的值'))
sum = 0
x = 2
for i in reversed(range(1, i + 1)):
    sum = x*(1/i+sum)
print(sum + 1)