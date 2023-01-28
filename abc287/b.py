# -*- coding: utf-8 -*-
N,M = map(int, input().split())
S = []
for i in range(N):
    S.append(input())

T = []
for j in range(M):
    T.append(input())

ans = 0
for i in range(N):
    for j in range(M):
        if S[i].endswith(T[j]):
            ans += 1
            break

print(ans)