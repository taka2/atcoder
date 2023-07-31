# -*- coding: utf-8 -*-
N = int(input())
xy = []
for i in range(N):
    x,y = map(int, input().split())
    xy.append((x,y))

ans = 0
for i in range(N):
    for j in range(i+1, N):
        p1 = xy[i]
        p2 = xy[j]
        a = (p1[1] - p2[1]) / (p1[0] - p2[0])
        if a >= -1 and a <= 1:
            ans += 1

print(ans)