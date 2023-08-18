# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))

subCount = [0] * N

for i in range(N-1):
    An = A[i]
    subCount[An-1] += 1

for i in range(N):
    print(subCount[i])