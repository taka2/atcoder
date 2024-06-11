# -*- coding: utf-8 -*-
from collections import deque
import math

# ユークリッド距離を求める
def getDistance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

N,D = map(int, input().split())
XY = []
for i in range(N):
    X,Y = map(int, input().split())
    XY.append((X,Y))

# ウイルス感染した人を管理する配列
virus = [False] * N
# 人1は感染
virus[0] = True

queue = deque()
queue.append(0)

while len(queue) > 0:
    elem = queue.popleft()
    for i in range(N):
        if i == elem:
            # 自分自身は除外
            pass
        elif virus[i]:
            # 感染済みは除外
            pass
        else:
            (X1, Y1) = XY[elem]
            (X2, Y2) = XY[i]
            distance = getDistance(X1, Y1, X2, Y2)
            if distance <= D:
                queue.append(i)
                virus[i] = True

for i in range(N):
    if virus[i]:
        print("Yes")
    else:
        print("No")