#!/usr/bin/python3
# p1
a = input()
val = pow(eval(a), 0.5)
val = "{0:.3f}".format(val)
print(val.rjust(30, "+"))