# -*- coding: utf-8 -*-
N = int(input())
XY = []
for i in range(N):
    X,Y = map(int, input().split())
    XY.append((X,Y))

ans = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            (x1,y1) = XY[i]
            (x2,y2) = XY[j]
            (x3,y3) = XY[k]

            judge = (x2-x1)*(y3-y1) - (x3-x1)*(y2-y1)
            if judge != 0:
                ans += 1

print(ans)