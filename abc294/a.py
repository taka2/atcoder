# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))

B = []
for i in range(N):
    if A[i] % 2 == 0:
        B.append(A[i])

print(*B)