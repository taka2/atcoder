# -*- coding: utf-8 -*-
N,X,Y = map(int, input().split())

Red = {N:1}
Blue = {}

currentLevel = N
for i in range(N, 1, -1):
    # 赤い宝石の処理
    redCount = Red[i]
    Red[i-1] = redCount
    if i in Blue:
        Blue[i] += redCount * X
    else:
        Blue[i] = redCount * X

    # 青い宝石の処理
    blueCount = Blue[i]
    Red[i-1] += blueCount
    Blue[i-1] = blueCount * Y

if 1 in Blue:
    print(Blue[1])
else:
    print(0)