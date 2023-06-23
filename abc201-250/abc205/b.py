# -*- coding: utf-8 -*-
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

mapA = defaultdict(int)

for i in range(N):
    mapA[A[i]] = 1

ans = True
for i in range(1, N+1):
    if i not in mapA:
        ans = False
        break

if ans:
    print("Yes")
else:
    print("No")