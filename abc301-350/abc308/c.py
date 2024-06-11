# -*- coding: utf-8 -*-
from collections import defaultdict
from decimal import *

N = int(input())
mapAB = defaultdict(list)
for i in range(N):
    A,B = map(int, input().split())
    successRate = Decimal(A)/Decimal(A+B)
    mapAB[successRate].append(i+1)

ans = []
sortedRate = sorted(list(mapAB), reverse=True)
for i in range(len(sortedRate)):
    numberList = sorted(mapAB[sortedRate[i]])
    for j in range(len(numberList)):
        ans.append(numberList[j])

print(*ans)