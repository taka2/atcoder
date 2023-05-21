# -*- coding: utf-8 -*-
N = int(input())

val = 1
for i in range(61):
    if val > N:
        print(i-1)
        break
    val *= 2
