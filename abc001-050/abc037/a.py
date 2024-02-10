# -*- coding: utf-8 -*-
A,B,C = map(int, input().split())

if A>B:
    print(C//B)
else:
    print(C//A)