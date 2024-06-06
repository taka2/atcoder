# -*- coding: utf-8 -*-
N = int(input())
W = []
for i in range(N):
    W.append(input())

mapW = {}
prevW = ""
ans = True
for i in range(N):
    currentW = W[i]
    if prevW != "" and prevW[-1] != currentW[0]:
        ans = False
        break
    if currentW in mapW:
        ans = False
        break
    mapW[currentW] = 1
    prevW = currentW

if ans:
    print("Yes")
else:
    print("No")