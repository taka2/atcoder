# -*- coding: utf-8 -*-
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

mapA = defaultdict(int)

for i in range(N):
    mapA[A[i]] += 1

ans = 0
for mapKey in mapA:
    num = mapA[mapKey]
    ans += num // 2

print(ans)