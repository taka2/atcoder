# -*- coding: utf-8 -*-
H,N = map(int, input().split())
A = list(map(int, input().split()))

sumA = 0
for i in range(N):
    sumA += A[i]

if sumA >= H:
    print("Yes")
else:
    print("No")
