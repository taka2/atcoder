# -*- coding: utf-8 -*-
N,M,C = map(int, input().split())
B = list(map(int, input().split()))
A = []
for i in range(N):
    Ai = list(map(int, input().split()))
    A.append(Ai)

ans = 0
for i in range(N):
    judge = 0
    for j in range(M):
        judge += A[i][j] * B[j]
    judge += C
    if judge > 0:
        ans += 1

print(ans)