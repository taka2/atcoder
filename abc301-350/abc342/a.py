# -*- coding: utf-8 -*-
S = input()
mapS = {}

for i in range(len(S)):
    if S[i] not in mapS:
        mapS[S[i]] = 1
    else:
        mapS[S[i]] += 1

target = ""
for key in mapS:
    if mapS[key] == 1:
        target = key
        break

print(S.find(target)+1)