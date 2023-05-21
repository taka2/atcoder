# -*- coding: utf-8 -*-
from collections import defaultdict
N,M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

mapA = defaultdict(int)
for i in range(N):
    mapA[A[i]] += 1

ans = True
for j in range(M):
    if B[j] not in mapA or mapA[B[j]] == 0:
        ans = False
        break
    mapA[B[j]] -= 1

if ans:
    print("Yes")
else:
    print("No")