# -*- coding: utf-8 -*-
def searchMax(p, index, max):
    maxValue = 0
    resultIndex = 0
    for i in range(index, len(p)):
        if(p[i] > maxValue and p[i] < max):
            maxValue = p[index]
            result = index

    return resultIndex

# 整数の入力
n = int(input())
p = list(map(int, input().split()))

baseList = list(range(n+1))
baseList.pop(0)

for i in range(len(p)):
    index = len(p) - i-1
    preIndex = index -1
    
    if(p[preIndex] > p[index]):
        max = searchMax(p, index, p[preIndex])
        tmp = p[preIndex]
        p[preIndex] = p[index]
        p[index] = tmp

print(p)