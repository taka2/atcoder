# -*- coding: utf-8 -*-
from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))

mapA = defaultdict(int)
for i in range(len(A)):
    mapA[A[i]] += 1

for j in mapA:
    if mapA[j] == 3:
        print(j)
        break