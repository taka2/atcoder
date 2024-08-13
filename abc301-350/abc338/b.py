# -*- coding: utf-8 -*-
S = input()
mapS = {}
for i in range(len(S)):
    if S[i] not in mapS:
        mapS[S[i]] = 1
    else:
        mapS[S[i]] += 1

maxCount = 0
for key in mapS:
    if mapS[key] > maxCount:
        maxCount = mapS[key]

ansList = []
for key in mapS:
    if mapS[key] == maxCount:
        ansList.append(key)

sortedAnsList = sorted(ansList)
print(sortedAnsList[0])