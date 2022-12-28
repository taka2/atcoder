# -*- coding: utf-8 -*-
from collections import defaultdict
N,X,Y = map(int, input().split())

Red = defaultdict(int)
Red[N] = 1
Blue = defaultdict(int)

currentLevel = N
for i in range(N, 1, -1):
    # 赤い宝石の処理
    redCount = Red[i]
    Red[i-1] = redCount
    Blue[i] += redCount * X

    # 青い宝石の処理
    blueCount = Blue[i]
    Red[i-1] += blueCount
    Blue[i-1] = blueCount * Y

if 1 in Blue:
    print(Blue[1])
else:
    print(0)