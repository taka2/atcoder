# -*- coding: utf-8 -*-
H,W = map(int, input().split())
S = []
for i in range(H):
    S.append(input())

for i in range(H):
    Si = S[i]
    for j in range(W-1):
        if Si[j] == 'T' and Si[j+1] == 'T':
            Si = Si[:j] + "PC" + Si[j+2:]
    print(Si)