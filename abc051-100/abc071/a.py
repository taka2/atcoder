# -*- coding: utf-8 -*-
x,a,b = map(int, input().split())

da = abs(x-a)
db = abs(x-b)

if da < db:
    print("A")
else:
    print("B")