# -*- coding: utf-8 -*-
N,S,D = map(int, input().split())
XY = []
for i in range(N):
    X,Y = map(int, input().split())
    XY.append((X,Y))

ans = False
for i in range(N):
    (X,Y) = XY[i]
    if X < S and Y > D:
        ans = True
        break

if ans:
    print("Yes")
else:
    print("No")