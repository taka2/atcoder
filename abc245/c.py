# -*- coding: utf-8 -*-
N,K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dpA = [True] + [False] * N
dpB = [True] + [False] * N

for i in range(1, N):
    if dpA[i-1]:
        if abs(A[i-1] - A[i]) <= K:
            dpA[i] = True
        if abs(A[i-1] - B[i]) <= K:
            dpB[i] = True

    if dpB[i-1]:
        if abs(B[i-1] - A[i]) <= K:
            dpA[i] = True
        if abs(B[i-1] - B[i]) <= K:
            dpB[i] = True

if dpA[N-1] or dpB[N-1]:
    print("Yes")
else:
    print("No")