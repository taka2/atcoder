# -*- coding: utf-8 -*-
N,M = map(int, input().split())
A = list(map(int, input().split()))

sumHW = 0
for i in range(M):
    sumHW += A[i]

if sumHW > N:
    print("-1")
else:
    print(N-sumHW)