# -*- coding: utf-8 -*-
N = int(input())

mapST = {}
ans = False
for i in range(N):
    S,T = input().split()
    key = S + "/" + T
    if key in mapST:
        ans = True
    mapST[key] = 1

if ans:
    print("Yes")
else:
    print("No")