# -*- coding: utf-8 -*-
A,B,C,X = map(int, input().split())

if X <= A:
    print(1)
elif X > A and X<=B:
    print(C/(B-A))
else:
    print(0)