# -*- coding: utf-8 -*-
N = int(input())
mapA = {}
for i in range(N):
    mapA[int(input())] = 1

sortedA = sorted(mapA)
print(sortedA[-2])

