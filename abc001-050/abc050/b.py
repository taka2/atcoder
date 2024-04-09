# -*- coding: utf-8 -*-
N = int(input())
T = list(map(int, input().split()))
M = int(input())
PX = []
for i in range(M):
    P,X = map(int, input().split())
    PX.append((P,X))

for i in range(M):
    ans = 0
    PXi = PX[i]
    for j in range(N):
        if j == PXi[0]-1:
            ans += PXi[1]
        else:
            ans += T[j]
    print(ans)