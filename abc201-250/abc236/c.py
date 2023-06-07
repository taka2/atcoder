# -*- coding: utf-8 -*-
N,M = map(int, input().split())
S = list(input().split())
T = list(input().split())

mapT = {}
for i in range(M):
    mapT[T[i]] = 1

for i in range(N):
    if S[i] in mapT:
        print("Yes")
    else:
        print("No")