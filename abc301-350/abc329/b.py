# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))

max1 = 0
for i in range(N):
    max1 = max(max1, A[i])

max2 = 0
for i in range(N):
    if A[i] != max1:
        max2 = max(max2, A[i])

print(max2)