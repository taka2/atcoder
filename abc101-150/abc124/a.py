# -*- coding: utf-8 -*-
A,B = map(int, input().split())

if A==B:
    print(A+B)
else:
    maxAB = max(A,B)
    print(maxAB*2-1)