# -*- coding: utf-8 -*-
N,M = map(int, input().split())
A = list(map(int, input().split()))

sumA = 0
for i in range(N):
    sumA += A[i]

sortedA = sorted(A, reverse=True)

picked = 0
for i in range(N):
    if sortedA[i]*4*M >= sumA:
        picked += 1

if picked >= M:
    print("Yes")
else:
    print("No")