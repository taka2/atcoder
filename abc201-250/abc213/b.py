# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))

sortedA = sorted(A)
boobieScore = sortedA[N-2]

for i in range(N):
    if A[i] == boobieScore:
        print(i+1)
        break