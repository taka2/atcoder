# -*- coding: utf-8 -*-
N,K = map(int, input().split())
A = list(map(int, input().split()))

mapN = {}
for i in range(N):
    mapN[A[i]] = 1

while(len(mapN) < K):
    list = list(mapN)
    for key in list:
        for i in range(N):
            mapN[key+A[i]] = 1

print(sorted(mapN)[K-1])