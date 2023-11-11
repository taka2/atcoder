# -*- coding: utf-8 -*-
N,M = map(int, input().split())
KA = []
for i in range(N):
    KAi = list(map(int, input().split()))
    KA.append(KAi)

ansMap = {}
for i in range(1,M+1):
    ansMap[i] = 0

for i in range(N):
    KAi = KA[i]
    for j in range(KAi[0]):
        num = KAi[j+1]
        ansMap[num] += 1

ans = 0
for i in range(1,M+1):
    if ansMap[i] == N:
        ans += 1

print(ans)