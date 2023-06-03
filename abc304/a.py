# -*- coding: utf-8 -*-
N = int(input())
SA = []
minValue = 10**9+1
minIndex = -1
for i in range(N):
    S,A = input().split()
    A = int(A)
    SA.append((S,A))
    minValue = min(minValue, A)
    if minValue == A:
        minIndex = i

for i in range(N):
    targetIndex = (i+minIndex) % N
    print(SA[targetIndex][0])