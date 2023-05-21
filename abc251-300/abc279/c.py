# -*- coding: utf-8 -*-
from collections import defaultdict
def countSharp(s):
    return s.count('#')

H,W = map(int, input().split())
S = []
T = []

for i in range(H):
    S.append(input())
for j in range(H):
    T.append(input())

counterS = defaultdict(int)
counterT = defaultdict(int)
for i in range(W):
    columnS = ""
    columnT = ""
    for j in range(H):
        columnS += S[j][i]
        columnT += T[j][i]
    counterS[columnS] += 1
    counterT[columnT] += 1

if len(counterS) != len(counterT):
    print("No")
    exit(0)

result = True
for i in counterS:
    if i not in counterT or counterS[i] != counterT[i]:
        result = False
        break

if(result):
    print("Yes")
else:
    print("No")