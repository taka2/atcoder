# -*- coding: utf-8 -*-
N = int(input())
P = list(map(int, input().split()))

maxP = 0
for i in range(1,N):
    maxP = max(maxP, P[i])
    
if P[0] > maxP:
    print("0")
else:
    print(maxP-P[0]+1)