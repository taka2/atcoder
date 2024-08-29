# -*- coding: utf-8 -*-
N = int(input())
P = list(map(int, input().split()))
mapP = {}
for i in range(N):
    mapP[P[i]] = i

Q = int(input())
for i in range(Q):
    A,B = map(int, input().split())
    orderA = mapP[A]
    orderB = mapP[B]
    if orderA < orderB:
        print(A)
    else:
        print(B)