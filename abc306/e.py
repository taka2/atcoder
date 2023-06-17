# -*- coding: utf-8 -*-
N,K,Q = map(int, input().split())
XY = []
for i in range(Q):
    X,Y = map(int, input().split())
    XY.append((X,Y))

total = 0
count = 0
minValue = 10**10
mapA = {}

for i in range(Q):
    (X,Y) = XY[i]
    if count < K:
        if X not in mapA:
            total += Y
            count += 1
            minValue = min(minValue, Y)
            mapA[X] = Y
        else:
            total = total + Y - mapA[X]
            minValue = min(minValue, Y)
            mapA[X] = Y
    else:
        if X not in mapA:
            if Y > minValue:
                total = total + Y - minValue
                minValue = Y
                mapA[X] = Y
            else:
                mapA[X] = Y
        else:
            if Y > mapA[X]:
                total = total + Y - mapA[X]
                