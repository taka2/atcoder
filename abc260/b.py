# -*- coding: utf-8 -*-
N,X,Y,Z = map(int, input().split())
# 数学の点数
A = list(map(int, input().split()))
# 英語の点数
B = list(map(int, input().split()))

resultList = []
# 1.数学の点が高い方から X 人を合格とする。
if X != 0:
    mathOKPoints = sorted(A)[N-X:N]
    result1 = 0
    for i in range(N):
        if A[i] in mathOKPoints:
            result1 += 1
            resultList.append(i+1)
            #print("1:", i+1)
        if result1 == X:
            break

# 2.次に、この時点でまだ合格となっていない受験者のうち、英語の点が高い方から Y 人を合格とする。
if Y != 0:
    englishPoints = []
    for i in range(N):
        if (i+1) not in resultList:
            englishPoints.append(B[i])
        else:
            englishPoints.append(-1)
    englishOKPoints = sorted(englishPoints)[len(englishPoints)-Y:len(englishPoints)]
    print(englishOKPoints)
    result2 = 0
    for i in range(N):
        if (i+1) not in resultList and englishPoints[i] in englishOKPoints:
            result2 += 1
            resultList.append(i+1)
            #print("2:", i+1)
        if result2 == Y:
            break

# 3.次に、この時点でまだ合格となっていない受験者のうち、数学と英語の合計点が高い方から Z 人を合格とする。
if Z != 0:
    sumPoints = []
    for i in range(N):
        if (i+1) not in resultList:
            sumPoints.append(A[i] + B[i])
        else:
            sumPoints.append(-1)
    sumOKPoints = sorted(sumPoints)[len(sumPoints)-Z:len(sumPoints)]
    print("sumOKPoints",sumOKPoints)
    result3 = 0
    for i in range(N):
        if (i+1) not in resultList and sumPoints[i] in sumOKPoints:
            result3 += 1
            resultList.append(i+1)
            #print("3:", i+1)
        if result3 == Z:
            break

for i in sorted(resultList):
    print(i)