# -*- coding: utf-8 -*-
N = int(input())

for i in range(1,10):
    if N <= i*111:
        print(i*111)
        break