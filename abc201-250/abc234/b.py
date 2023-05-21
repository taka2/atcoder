# -*- coding: utf-8 -*-
import math

N = int(input())
xy = []
for i in range(N):
    x,y = map(int, input().split())
    xy.append((x,y))

def len(p1, p2):
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    return math.sqrt(abs(x2-x1)**2 + abs(y2-y1)**2)

ans = 0
for i in range(N):
    for j in range(N):
        if i==j:
            continue
        length = len(xy[i], xy[j])
        ans = max(ans, length)

print(ans)