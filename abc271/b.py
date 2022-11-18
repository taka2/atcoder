# -*- coding: utf-8 -*-
# 整数の入力
n,q = map(int,input().split())

numList = [""]
for i in range(n):
    numList.append(list(map(int, input().split())))

for i in range(q):
    query = list(map(int, input().split()))
    print(numList[query[0]][query[1]])