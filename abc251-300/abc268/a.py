# -*- coding: utf-8 -*-
# スペース区切りの整数の入力
numList = list(map(int, input().split()))

map = {}
for i in numList:
    map[i] = 1

print(len(map))
