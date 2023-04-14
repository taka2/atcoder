# -*- coding: utf-8 -*-
from collections import defaultdict

def combination(n,r):
    return n*(n-1)*(n-2)//6

N = int(input())
A = list(map(int, input().split()))

mapA = defaultdict(int)
for i in range(1,101):
    mapA[i] = 0
for i in range(N):
    mapA[A[i]] += 1

ans = 0
for i in range(1, 101):
    if mapA[i] >= 3:
        ans += combination(mapA[i], 3)

print(ans)