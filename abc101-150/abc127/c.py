# -*- coding: utf-8 -*-
N,M = map(int, input().split())
LR = []
for i in range(M):
    L,R = map(int, input().split())
    LR.append((L,R))

Lmax = 0
Rmin = 10**5
for i in range(M):
    (L,R) = LR[i]
    Lmax = max(Lmax, L)
    Rmin = min(Rmin, R)

if Rmin-Lmax>=0:
    print(Rmin-Lmax+1)
else:
    print(0)