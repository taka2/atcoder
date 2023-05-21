# -*- coding: utf-8 -*-
# 整数の入力
n, k = map(int, input().split())
numList = list(map(int, input().split()))

resultList = []
for i in range(n):
    if(i+k >= n):
        resultList.append(0)
    else:
        resultList.append(numList[i+k])

print(" ".join(map(str, resultList)))