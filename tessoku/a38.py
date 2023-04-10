# -*- coding: utf-8 -*-
D,N = map(int, input().split())
LRH = []
for i in range(N):
    L,R,H = map(int, input().split())
    LRH.append((L,R,H))

LIM = [0] + [24] * (D)
for i in range(1,D+1):
    for j in range(N):
        (L,R,H) = LRH[j]
        if i >= L and i <= R:
            LIM[i] = min(LIM[i], H)

print(sum(LIM))