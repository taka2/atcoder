# -*- coding: utf-8 -*-
N,K = map(int, input().split())
ansN = [False] * N
for i in range(K):
    d = int(input())
    A = list(map(int, input().split()))
    for j in range(d):
        ansN[A[j]-1] = True

ans = 0
for i in range(N):
    if ansN[i] == False:
        ans += 1

print(ans)