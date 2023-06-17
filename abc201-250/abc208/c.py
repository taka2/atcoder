# -*- coding: utf-8 -*-
N,K = map(int, input().split())
a = list(map(int, input().split()))

sortedA = sorted(a)
mapA = {}
for i in range(N):
    mapA[a[i]] = i+1

ansList = [0] * (N+1)
amari = K%N
for i in range(N):
    num = sortedA[i]
    ind = mapA[num]
    ansList[ind] = K//N
    if amari > 0:
        ansList[ind] += 1
        amari -= 1

ansList = ansList[1:]
for i in range(len(ansList)):
    print(ansList[i])