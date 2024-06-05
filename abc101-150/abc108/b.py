# -*- coding: utf-8 -*-
x1,y1,x2,y2 = map(int, input().split())

dx = x2 - x1
dy = y2 - y1
x = x2
y = y2

ans = []
for i in range(2):
    _dx = -dy
    _dy = dx
    dx = _dx
    dy = _dy

    x = x + dx
    y = y + dy

    ans.append((x,y))

print(ans[0][0], ans[0][1], ans[1][0], ans[1][1])