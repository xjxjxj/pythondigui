#!/usr/bin/evn.python
# _*_coding:utf-8_*_
# @Author:xj
def fact(j):
    sum = 0
    if j == 0:
        sum = 1
    else:
        sum = j * fact(j - 1)
    return sum
for i in range(10):
    print("%d! = %d" %(i,fact(i)))
