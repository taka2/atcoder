# -*- coding: utf-8 -*-
N = int(input())
S = []
for i in range(N):
    S.append(input())

mapA = {}
mapB = {}
ans = "satisfiable"
for i in range(N):
    Si = S[i]
    if Si[0] == '!':
        key = Si[1:]
        if key in mapB:
            ans = key
            break
        else:
            mapA[key] = 1
    else:
        key = Si
        if key in mapA:
            ans = key
            break
        else:
            mapB[key] = 1

print(ans)