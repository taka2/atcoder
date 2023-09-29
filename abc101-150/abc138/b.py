# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))

sumReverseA = 0
for i in range(N):
    sumReverseA += 1/A[i]

print(1/sumReverseA)