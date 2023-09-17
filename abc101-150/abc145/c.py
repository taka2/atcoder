# -*- coding: utf-8 -*-
import itertools
import math

N = int(input())
xy = []
for i in range(N):
    x,y = map(int, input().split())
    xy.append((x,y))

def calcDistance(i, j):
    (x1,y1) = xy[i]
    (x2,y2) = xy[j]
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

distances = []
for elem in itertools.permutations(list(range(N))):
    distance = 0
    for i in range(len(elem)-1):
        distance += calcDistance(elem[i], elem[i+1])
    distances.append(distance)

sumDistance = 0
for i in range(len(distances)):
    sumDistance += distances[i]

print(sumDistance / len(distances))
