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

directions = [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)]
result = 0
for i in range(N):
    for j in range(N):
        baseZahyo = (i,j)
        for k in range(len(directions)):
            direction = directions[k]
            zahyoList = getZahyoList(baseZahyo, direction[0], direction[1])
            value = getValueFromZahyoList(zahyoList)
            if value > result:
                result = value

print(result)