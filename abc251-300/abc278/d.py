# -*- coding: utf-8 -*-
n = int(input())
numberList = list(map(int, input().split()))
numberMap = {}
for i in range(n):
    numberMap[i+1] = numberList[i]
base = 0

q = int(input())
for i in range(q):
    operation = list(map(int, input().split()))
    t = operation[0]
    if t == 1:
        value = operation[1]
        numberMap = {}
        base = value
    elif t == 2:
        index = operation[1]
        value = operation[2]
        if index in numberMap:
            numberMap[index] += value
        else:
            numberMap[index] = value
    elif t == 3:
        index = operation[1]
        if index in numberMap:
            print(base + numberMap[index])
        else:
            print(base)