# -*- coding: utf-8 -*-
from collections import defaultdict

S = input()

mapS = defaultdict(int)

for i in range(4):
    mapS[S[i]] += 1

keys = list(mapS.keys())
if len(mapS) == 2 and mapS[keys[0]] == 2 and mapS[keys[1]] == 2:
    print("Yes")
else:
    print("No")