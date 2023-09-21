# -*- coding: utf-8 -*-
from collections import defaultdict

N,K,Q = map(int, input().split())
A = []
for i in range(Q):
    A.append(int(input()))

mapA = defaultdict(int)
for i in range(Q):
    mapA[A[i]] += 1

for i in range(N):
    if K - Q + mapA[i+1] > 0:
        print("Yes")
    else:
        print("No")