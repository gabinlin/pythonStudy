#!/usr/bin/python3
from random import random
from time import perf_counter

# 1、公式算法
pi = 0
N = 1000
for k in range(N):
    pi += 1/pow(16,k) * (4/(8*k+1) - 2/(8*k+4) - 1/(8*k+5) - 1/(8*k+6))
print("圆周率值是:{}".format(pi))

# 2、投点算法（随机数算法）
pi = 0
DARTS = 1000 * 1000
hits = 0.0
start = perf_counter()
for i in range(1, DARTS+1):
    x, y = random(), random()
    ## 直角三角形的求边公式，两短边平方和等于第三斜长边平方和
    dist = pow(x ** 2 + y ** 2, 0.5)
    if dist <= 1.0:
        hits += 1
pi = 4 * (hits/DARTS)
print("圆周率值是:{}".format(pi))
print("运行时间是:{:.5f}s".format(perf_counter() - start))