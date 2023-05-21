# -*- coding: utf-8 -*-
from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))

mapA = defaultdict(int)
for i in range(N):
    mapA[A[i]] = 1

print(len(mapA))