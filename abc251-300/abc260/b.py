# -*- coding: utf-8 -*-
N,X,Y,Z = map(int, input().split())
# 数学の点数
A = list(map(int, input().split()))
# 英語の点数
B = list(map(int, input().split()))

# 数学の点数リスト
mathList = []
for i in range(N):
    mathList.append((i+1, A[i]))
mathList = sorted(mathList, key=lambda x: x[1], reverse=True)
#print(mathList)

# 英語の点数リスト
englishList = []
for i in range(N):
    englishList.append((i+1, B[i]))
englishList = sorted(englishList, key=lambda x: x[1], reverse=True)
#print(englishList)

# 合計点のリスト
totalList = []
for i in range(N):
    totalList.append((i+1, A[i] + B[i]))
totalList = sorted(totalList, key=lambda x: x[1], reverse=True)
#print(totalList)

resultList = []
for i in range(X):
    targetNumber = mathList[i][0]
    resultList.append(targetNumber)
#print(resultList)

countY = 0
for i in range(N):
    if countY == Y:
        break
    targetNumber = englishList[i][0]
    if targetNumber not in resultList:
        resultList.append(targetNumber)
        countY += 1
#print(resultList)

countZ = 0
for i in range(N):
    if countZ == Z:
        break
    targetNumber = totalList[i][0]
    if targetNumber not in resultList:
        resultList.append(targetNumber)
        countZ += 1
#print(resultList)

for i in sorted(resultList):
    print(i)
