# -*- coding: utf-8 -*-
N,X = map(int, input().split())
A = list(map(int, input().split()))

Adash = []
for i in range(N):
    if A[i] != X:
        Adash.append(A[i])

print(*Adash)