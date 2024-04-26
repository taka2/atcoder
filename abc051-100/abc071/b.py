# -*- coding: utf-8 -*-
from collections import defaultdict

S = input()
mapS = defaultdict(int)

for i in range(len(S)):
    mapS[S[i]] += 1

alpha = "abcdefghijklmnopqrstuvwxyz"

ans = "None"
for i in range(len(alpha)):
    if alpha[i] not in mapS:
        ans = alpha[i]
        break

print(ans)