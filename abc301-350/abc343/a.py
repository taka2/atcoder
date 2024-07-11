# -*- coding: utf-8 -*-
A,B = map(int, input().split())
for i in range(0,10):
    if (A+B) != i:
        print(i)
        break