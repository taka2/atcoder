# -*- coding: utf-8 -*-
L,H = map(int, input().split())
N = int(input())
A = []
for i in range(N):
    A.append(int(input()))

for i in range(N):
    if A[i] < L:
        print(L-A[i])
    elif A[i] > H:
        print(-1)
    else:
        print(0)