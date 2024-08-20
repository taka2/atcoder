# -*- coding: utf-8 -*-
N = int(input())

for i in range(N, 920):
    a = i // 100
    b = (i - a*100) // 10
    c = i % 10

    if a * b == c:
        print(i)
        break