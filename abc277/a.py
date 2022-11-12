# -*- coding: utf-8 -*-
# 整数の入力
n, x = map(int, input().split())
numList = list(map(int, input().split()))

for i in range(len(numList)):
    if numList[i] == x:
        print(i+1)