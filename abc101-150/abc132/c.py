# -*- coding: utf-8 -*-
N = int(input())
d = list(map(int, input().split()))

sortedD = sorted(d)

leftIndex = N//2-1
rightIndex = N//2

if sortedD[leftIndex] == sortedD[rightIndex]:
    print(0)
else:
    print(sortedD[rightIndex] - sortedD[leftIndex])