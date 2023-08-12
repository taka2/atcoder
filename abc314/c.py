# -*- coding: utf-8 -*-
from collections import defaultdict

N,M = map(int, input().split())
S = input()
listS = list(S)
C = list(map(int, input().split()))

firstPositionByColor = defaultdict(int)
prevCharByColor = defaultdict(str)

for i in range(N):
    Si = S[i]
    Ci = C[i]
    if Ci not in firstPositionByColor:
        firstPositionByColor[Ci] = i
    if Ci in prevCharByColor:
        listS[i] = prevCharByColor[Ci]
        prevCharByColor[Ci] = Si
    else:
        prevCharByColor[Ci] = Si

for j in range(1,M+1):
    listS[firstPositionByColor[j]] = prevCharByColor[j]

ans = ""
for i in range(len(listS)):
    ans += listS[i]

print(ans)