# -*- coding: utf-8 -*-
N = int(input())
A = []
for i in range(N):
    A.append(int(input()))

sortedA = sorted(A, reverse=True)

for i in range(N):
    if A[i] == sortedA[0]:
        print(sortedA[1])
    else:
        print(sortedA[0])
