# -*- coding: utf-8 -*-
N = int(input())
A = []
for i in range(N):
    A.append(list(map(int, input())))

def getZahyoList(baseZahyo, tate, yoko):
    resultList = [baseZahyo]

    zahyo = baseZahyo
    for i in range(N-1):
        zahyo = ((zahyo[0]+tate+N)%N, (zahyo[1]+yoko+N)%N)
        resultList.append(zahyo)
    return resultList

def getValueFromZahyoList(zahyoList):
    resultValue = 0
    for i in range(N):
        value = A[zahyoList[i][0]][zahyoList[i][1]]
        resultValue += (value * 10**(N-i-1))
    return resultValue

result = 0
for i in range(N):
    for j in range(N):
        baseZahyo = (i,j)
        upZahyoList = getZahyoList(baseZahyo, -1, 0)
        upValue = getValueFromZahyoList(upZahyoList)
        if upValue > result:
            result = upValue
        downZahyoList = getZahyoList(baseZahyo, 1, 0)
        downValue = getValueFromZahyoList(downZahyoList)
        if downValue > result:
            result = downValue
        leftZahyoList = getZahyoList(baseZahyo, 0, -1)
        leftValue = getValueFromZahyoList(leftZahyoList)
        if leftValue > result:
            result = leftValue
        rightZahyoList = getZahyoList(baseZahyo, 0, 1)
        rightValue = getValueFromZahyoList(rightZahyoList)
        if rightValue > result:
            result = rightValue
        upLeftZahyoList = getZahyoList(baseZahyo, -1, -1)
        upLeftValue = getValueFromZahyoList(upLeftZahyoList)
        if upLeftValue > result:
            result = upLeftValue
        upRightZahyoList = getZahyoList(baseZahyo, -1, 1)
        upRightValue = getValueFromZahyoList(upRightZahyoList)
        if upRightValue > result:
            result = upRightValue
        downLeftZahyoList = getZahyoList(baseZahyo, 1, -1)
        downLeftValue = getValueFromZahyoList(downLeftZahyoList)
        if downLeftValue > result:
            result = downLeftValue
        downRightZahyoList = getZahyoList(baseZahyo, 1, 1)
        downRightValue = getValueFromZahyoList(downRightZahyoList)
        if downRightValue > result:
            result = downRightValue

print(result)