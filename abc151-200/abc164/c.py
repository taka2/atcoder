# -*- coding: utf-8 -*-
from collections import defaultdict

N = int(input())
ansMap = defaultdict(int)
for i in range(N):
    S = input()
    ansMap[S] += 1

print(len(ansMap))