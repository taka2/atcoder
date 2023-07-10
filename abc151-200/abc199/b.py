# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

maxA = max(A)
minB = min(B)

if minB < maxA:
    print("0")
else:
    print(minB - maxA + 1)