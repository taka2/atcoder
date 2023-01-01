# -*- coding: utf-8 -*-
import math

N,K = map(int, input().split())
A = list(map(int, input().split()))
Amap = {}
for i in range(len(A)):
    Amap[A[i]-1] = 1

XY = []
for i in range(N):
    XY.append(list(map(int, input().split())))

def calcDistance(XY1, XY2):
    return math.sqrt((XY1[0]-XY2[0])**2 + (XY1[1]-XY2[1])**2)

result = 0
for i in range(N):
    # 明かりを持っている人はチェックしない
    if i in Amap:
        continue

    mindistance = 999999999999999999999999
    for j in range(N):
        # 自分自身はチェックしない
        if i == j:
            continue
        # 明かりを持ってない人はチェックしない
        if j not in Amap:
            continue

        distance = calcDistance(XY[i], XY[j])
        if distance < mindistance:
            mindistance = distance
    
    if mindistance > result:
        result = mindistance

print(result)
