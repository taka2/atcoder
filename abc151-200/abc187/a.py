# -*- coding: utf-8 -*-
A,B = map(int, input().split())
SA = A // 100 + A % 100 // 10 + A % 10
SB = B // 100 + B % 100 // 10 + B % 10

if SA > SB:
    print(SA)
else:
    print(SB)