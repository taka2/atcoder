# -*- coding: utf-8 -*-
import math

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

k = int(input())
fact = factorization(k)
loopCount = 1
for i in fact:
    #print(i)
    loopCount *= (i[1]+1)

values = []
for i in range(loopCount):
    #print("i=",i)
    value = 1
    tmpi = i
    for j in range(len(fact)):
        indexJ = tmpi % (fact[j][1]+1)
        tmpi //= (fact[j][1]+1)
        value *= fact[j][0] ** indexJ
        #print("indexJ=", indexJ, "value=", value)
    values.append(value)

sortedValues = sorted(values)
#print(sortedValues)

for i in range(len(sortedValues)):
    if sortedValues[i] >= k and sortedValues % k == 0:
        print(sortedValues[i])
        break