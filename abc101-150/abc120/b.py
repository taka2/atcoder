# -*- coding: utf-8 -*-
A,B,K = map(int, input().split())

ansList = []
for i in range(1,101):
    if A % i == 0 and B % i == 0:
        ansList.append(i)

sortedAnsList = sorted(ansList, reverse=True)
print(sortedAnsList[K-1])