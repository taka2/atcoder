# -*- coding: utf-8 -*-
N,M,X = map(int, input().split())
A = list(map(int, input().split()))

cost0 = 0
costN = 0

for i in range(X+1, N+1):
    if i in A:
        cost0 += 1

for i in range(0, X):
    if i in A:
        costN += 1
    
print(min(cost0, costN))