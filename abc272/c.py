# -*- coding: utf-8 -*-
num = input()
numList = list(map(int, input().split()))

odds = []
evens = []
for i in numList:
    if i % 2 == 0:
        evens.append(i)
    else:
        odds.append(i)

evens = sorted(evens)
odds = sorted(odds)

if len(odds) <= 1 and len(evens) <= 1:
    print(-1)
else:
    oddsMaxIndex = len(odds)-1
    evensMaxIndex = len(evens)-1
    oddsMax = 0
    if oddsMaxIndex >= 1:
        oddsMax = odds[oddsMaxIndex-1] + odds[oddsMaxIndex]
    evensMax = 0
    if evensMaxIndex >= 1:
        evensMax = evens[evensMaxIndex-1] + evens[evensMaxIndex]
    print(max(oddsMax, evensMax))