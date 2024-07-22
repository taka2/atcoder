# -*- coding: utf-8 -*-
H = int(input())

current = 0
for i in range(1,10000):
    current += (2 ** (i-1))
    if current > H:
        print(i)
        break