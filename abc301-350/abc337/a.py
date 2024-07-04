# -*- coding: utf-8 -*-
N = int(input())
XY = []
for i in range(N):
    (X,Y) = map(int, input().split())
    XY.append((X,Y))

takahashi = 0
aoki = 0
for i in range(N):
    (X,Y) = XY[i]
    takahashi += X
    aoki += Y

if takahashi > aoki:
    print("Takahashi")
elif aoki > takahashi:
    print("Aoki")
else:
    print("Draw")