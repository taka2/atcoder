# -*- coding: utf-8 -*-
N,M= map(int, input().split())

A = list(map(int, input().split()))
B = list(range(1,N+1))

for i in range(1,M+1):
    posone = 1
    for k in range(1,M+1):
        if k==i:
            continue
        if A[k-1] == posone:
            posone += 1
        elif A[k-1] == (posone-1):
            posone -= 1
    print(posone)