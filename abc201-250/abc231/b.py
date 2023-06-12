# -*- coding: utf-8 -*-
from collections import defaultdict
 
N = int(input())
mapS = defaultdict(int)
for i in range(N):
  S = input()
  mapS[S] += 1
 
maxCount = 0
maxValue = ""
for S in mapS:
  if mapS[S] > maxCount:
    maxCount = mapS[S]
    maxValue = S
   
print(maxValue)