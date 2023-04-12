# -*- coding: utf-8 -*-
N = int(input())
LR = []
for i in range(N):
    L,R = map(int, input().split())
    LR.append((L,R))

# Rの小さい順にソート
LR.sort(key = lambda x: x[1])

ans = 0
current = 0
for i in range(N):
    (L,R) = LR[i]
    if L >= current:
        ans += 1
        current = R

print(ans)    