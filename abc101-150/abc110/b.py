# -*- coding: utf-8 -*-
N,M,X,Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

sortedX = sorted(x)
sortedY = sorted(y)

if sortedX[-1] < sortedY[0] and X < sortedY[0] and Y > sortedX[-1]:
    print("No War")
else:
    print("War")