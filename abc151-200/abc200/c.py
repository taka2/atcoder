# -*- coding: utf-8 -*-
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

# 200で割った余りの個数
mapA = defaultdict(int)
for i in range(N):
    mod200 = A[i] % 200
    mapA[mod200] += 1

ans = 0
for mapAkey in mapA:
    mapAvalue = mapA[mapAkey]
    ans += mapAvalue * (mapAvalue-1) // 2

print(ans) 