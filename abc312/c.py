# -*- coding: utf-8 -*-
from collections import defaultdict

N,M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

mapA = defaultdict(int)
mapB = defaultdict(int)

for i in range(N):
    mapA[A[i]] += 1

for i in range(M):
    mapB[B[i]] += 1

sumA = []
countA = 0
for mapAKey in sorted(mapA):
    countA += mapA[mapAKey]
    sumA.append((mapAKey, countA))

sumB = []
countB = 0
for mapBKey in sorted(mapB, reverse=True):
    countB += mapB[mapBKey]
    sumB.append((mapBKey, countB))

i = 0
j = 0
kai = 0
uri = 0
price = 0

while True:
    if i == len(sumA) and j == len(sumB):
        break
    if i == len(sumA):
        i = len(sumA)-1
    if j == len(sumB):
        j = len(sumB)-1
    sumAi = sumA[i]
    sumBj = sumB[j]
    if sumAi[0] <= sumBj[0]:
        uri += sumAi[1]
        i += 1
        kai += sumBj[1]
        j += 1
        price = sumAi[0]
    else:
        break

if price == 0 or kai > uri:
    print(sumB[0][0]+1)
else:
    print(price)