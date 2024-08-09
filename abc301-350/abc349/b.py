# -*- coding: utf-8 -*-
from collections import defaultdict

S = input()
mapS = defaultdict(int)

for i in range(len(S)):
    mapS[S[i]] += 1

mapT = defaultdict(int)
for key in mapS:
    mapT[mapS[key]] += 1

ans = True
for key in mapT:
    if mapT[key] == 0 or mapT[key] == 2:
        pass
    else:
        ans = False
        break

if ans:
    print("Yes")
else:
    print("No")