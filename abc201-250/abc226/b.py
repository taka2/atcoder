# -*- coding: utf-8 -*-
N = int(input())
mapLa = {}
for i in range(N):
    La = list(map(int, input().split()))
    mapLa[str(La)] = 1

print(len(mapLa))