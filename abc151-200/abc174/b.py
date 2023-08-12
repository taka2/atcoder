# -*- coding: utf-8 -*-
import math

N,D = map(int, input().split())
XY = []
for i in range(N):
    X,Y = map(int, input().split())
    XY.append((X,Y))

ans = 0
for i in range(N):
    (X,Y) = XY[i]
    distance = math.sqrt(X**2+Y**2)
    if distance <= D:
        ans += 1

print(ans)