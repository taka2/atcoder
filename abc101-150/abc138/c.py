# -*- coding: utf-8 -*-
N = int(input())
v = list(map(int, input().split()))

sortedV = sorted(v)

prev = 0
for i in range(1,N):
    if i == 1:
        prev = (sortedV[i-1] + sortedV[i])/2
    else:
        prev = (prev + sortedV[i])/2

print(prev)