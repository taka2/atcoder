# -*- coding: utf-8 -*-
N = int(input())
S = list(input().split())

mapS = {}
for i in range(N):
    if S[i] in mapS:
        mapS[S[i]] += 1
    else:
        mapS[S[i]] = 1

if len(mapS) == 4:
    print("Four")
else:
    print("Three")