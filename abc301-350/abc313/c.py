# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))

sumA = 0
for i in range(N):
    sumA += A[i]

avgA = sumA//N
shousuu = sumA/N-avgA
if sumA % N != 0 and shousuu >= 0.5:
    avgA += 1

opeCountPlus = 0
opeCountPlusCount = 0
opeCountMinus = 0
opeCountMinusCount = 0
for i in range(N):
    if A[i] == avgA:
        pass
    elif A[i] < avgA:
        opeCountPlus += avgA-A[i]
        opeCountPlusCount += 1
    else:
        opeCountMinus += A[i]-avgA
        opeCountMinusCount += 1

minOpe = min(opeCountPlus, opeCountMinus)
if opeCountPlus > opeCountMinus and opeCountPlusCount <= (opeCountPlus-opeCountMinus):
    ans = minOpe + (opeCountPlus - opeCountMinus) - opeCountPlusCount
elif opeCountPlus < opeCountMinus and opeCountMinusCount <= (opeCountMinus-opeCountPlus):
    ans = minOpe + (opeCountMinus - opeCountPlus) - opeCountMinusCount
else:
    ans = minOpe
print(ans)