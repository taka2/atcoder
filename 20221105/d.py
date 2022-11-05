# -*- coding: utf-8 -*-
import itertools

def checkIsAllOne(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]

    return (len(list) == sum)

# 整数の入力
n = int(input())
a = list(map(int, input().split()))

isAllOne = True
isContainsPrimeNumber = False
for i in range(len(a)):
    # print(a[i], a[i] %2, a[i] %3)
    if a[i] != 1:
        # print("isAllOne")
        isAllOne = False
    if a[i] != 1 and a[i] % 2 != 0 and a[i] % 3 != 0:
        # print("isContainsPrimeNumber")
        isContainsPrimeNumber = True
        break

if(isAllOne):
    print("0")
    exit
elif(isContainsPrimeNumber):
    print("-1")
    exit
else:
    # 計算開始
    count = 0
    workList = a
    # print("initial worklist = ", workList)
    while True:
        # print(workList)
        if(checkIsAllOne(workList)):
            break

        for i in range(len(workList)):
            if(workList[i] % 2 == 0):
                workList[i] = int(workList[i] / 2)
                count += 1
            if(workList[i] % 3 == 0):
                workList[i] = int(workList[i] / 3)
                count += 1

    print(count)
