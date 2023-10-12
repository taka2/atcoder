# -*- coding: utf-8 -*-
A,B,C = map(int, input().split())

if B//A >= C:
    print(C)
else:
    print(B//A)