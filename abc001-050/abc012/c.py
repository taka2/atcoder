# -*- coding: utf-8 -*-
N = int(input())

sumkuku = 0
for i in range(1,10):
    for j in range(1,10):
        sumkuku += i*j

kake = sumkuku - N
for i in range(1,10):
    for j in range(1,10):
        mult = i*j
        if mult == kake:
            print(i, "x", j)