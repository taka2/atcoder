# -*- coding: utf-8 -*-
A,D = map(int, input().split())

x1 = (A+1)*D
x2 = A*(D+1)

if x1 >= x2:
    print(x1)
else:
    print(x2)