# -*- coding: utf-8 -*-
from collections import defaultdict

N = int(input())

map = defaultdict(int)
for i in range(N):
    A = int(input())
    map[A] += 1

ans = 0
for key in map:
    N = map[key]
    if N > 1:
        ans += (N*(N-1)//2)

print(ans)