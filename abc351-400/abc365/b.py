# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))

sortedA = sorted(A)

secondLargeNumber = sortedA[-2]

for i in range(N):
    if A[i] == secondLargeNumber:
        print(i+1)
        break