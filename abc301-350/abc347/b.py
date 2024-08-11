# -*- coding: utf-8 -*-
S = input()

mapS = {}
for i in range(len(S)):
    for j in range(len(S)-i):
        subS = S[j:(j+i+1)]
        if subS not in mapS:
            mapS[subS] = 1

print(len(mapS))