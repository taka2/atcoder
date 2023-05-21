# -*- coding: utf-8 -*-
N = int(input())
XY = []
for i in range(N):
    (x,y) = map(int, input().split())
    XY.append((x,y))
S = input()

mapYR = {}
mapYL = {}
ans = False
for i in range(N):
    (x, y) = XY[i]
    if S[i] == 'R' and y not in mapYR:
        mapYR[y] = x
    elif S[i] == 'L' and y not in mapYL:
        mapYL[y] = x

    if S[i] == 'R' and y in mapYL and mapYL[y] > x:
        ans = True
        break
    if S[i] == 'L' and y in mapYR and mapYR[y] < x:
        ans = True
        break
    if S[i] == 'R' and x < mapYR[y]:
        mapYR[y] = x
    if S[i] == 'L' and x > mapYL[y]:
        mapYL[y] = x

if ans:
    print("Yes")
else:
    print("No")