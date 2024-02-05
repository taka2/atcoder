# -*- coding: utf-8 -*-
from collections import defaultdict

A,B,C = map(int, input().split())

mapA = defaultdict(int)
mapA[A] += 1
mapA[B] += 1
mapA[C] += 1

if mapA[5] == 2 and mapA[7] == 1:
    print("YES")
else:
    print("NO")