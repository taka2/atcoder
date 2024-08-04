# -*- coding: utf-8 -*-
N, A = map(int, input().split())
T = list(map(int, input().split()))

current = 0
for i in range(N):
    if T[i] > current:
        current = T[i]
    current += A
    print(current)
