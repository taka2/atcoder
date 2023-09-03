# -*- coding: utf-8 -*-
N = int(input())
X = list(map(int, input().split()))

ans = 99999999
for i in range(1,101):
    consumeVitalSum = 0
    for j in range(N):
        consumeVital = (X[j]-i)**2
        consumeVitalSum += consumeVital
    ans = min(ans, consumeVitalSum)

print(ans)