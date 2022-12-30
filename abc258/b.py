# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10000000)

N = int(input())
A = []
for i in range(N):
    A.append(list(map(int, input())))
#print(N, A)

# 盤面上の最大値を特定する
maxNumber = 0
for i in range(N):
    for j in range(N):
        if A[i][j] > maxNumber:
            maxNumber = A[i][j]

# 盤面上の最大値を持つ座標を特定する（複数の可能性あり）
maxNumberZahyoList = []
for i in range(N):
    for j in range(N):
        if A[i][j] == maxNumber:
            maxNumberZahyoList.append((i,j))
#print(maxNumberZahyoList)


def search(path):
    if len(path) == N:
        return path

    lastZahyo = path[-1]
    prevZahyo = None
    if len(path) >= 2:
        prevZahyo = path[-2]

    upZahyo = ((lastZahyo[0]-1+N)%N, lastZahyo[1])
    upValue = A[upZahyo[0]][upZahyo[1]] if upZahyo != prevZahyo else 0
    downZahyo = ((lastZahyo[0]+1)%N, lastZahyo[1])
    downValue = A[downZahyo[0]][downZahyo[1]] if downZahyo != prevZahyo else 0
    leftZahyo = (lastZahyo[0], (lastZahyo[1]-1+N)%N)
    leftValue = A[leftZahyo[0]][leftZahyo[1]] if leftZahyo != prevZahyo else 0
    rightZahyo = (lastZahyo[0], (lastZahyo[1]+1)%N)
    rightValue = A[rightZahyo[0]][rightZahyo[1]] if rightZahyo != prevZahyo else 0
    upLeftZahyo = ((lastZahyo[0]-1+N)%N, (lastZahyo[1]-1+N)%N)
    upLeftValue = A[upLeftZahyo[0]][upLeftZahyo[1]] if upLeftZahyo != prevZahyo else 0
    upRightZahyo = ((lastZahyo[0]-1+N)%N, (lastZahyo[1]+1)%N)
    upRightValue = A[upRightZahyo[0]][upRightZahyo[1]] if upRightZahyo != prevZahyo else 0
    downLeftZahyo = ((lastZahyo[0]+1)%N, (lastZahyo[1]-1+N)%N)
    downLeftValue = A[downLeftZahyo[0]][downLeftZahyo[1]] if downLeftZahyo != prevZahyo else 0
    downRightZahyo = ((lastZahyo[0]+1)%N, (lastZahyo[1]+1)%N)
    downRightValue = A[downRightZahyo[0]][downRightZahyo[1]] if downRightZahyo != prevZahyo else 0

    resultList = []
    maxValue = max(upValue, downValue, leftValue, rightValue, upLeftValue, upRightValue, downLeftValue, downRightValue)
    print(path, lastZahyo, upZahyo, downZahyo, leftZahyo, rightZahyo, upLeftZahyo, upRightZahyo, downLeftZahyo, downRightZahyo, maxValue)
    if upValue == maxValue and upZahyo != prevZahyo:
        path.append(upZahyo)
        resultList.append(search(path))
        path.pop()
    if downValue == maxValue and downZahyo != prevZahyo:
        path.append(downZahyo)
        resultList.append(search(path))
        path.pop()
    if leftValue == maxValue and leftZahyo != prevZahyo:
        path.append(leftZahyo)
        resultList.append(search(path))
        path.pop()
    if rightValue == maxValue and rightZahyo != prevZahyo:
        path.append(rightZahyo)
        resultList.append(search(path))
        path.pop()
    if upLeftValue == maxValue and upLeftZahyo != prevZahyo:
        path.append(upLeftZahyo)
        resultList.append(search(path))
        path.pop()
    if upRightValue == maxValue and upRightZahyo != prevZahyo:
        path.append(upRightZahyo)
        resultList.append(search(path))
        path.pop()
    if downLeftValue == maxValue and downLeftZahyo != prevZahyo:
        path.append(downLeftZahyo)
        resultList.append(search(path))
        path.pop()
    if downRightValue == maxValue and downRightZahyo != prevZahyo:
        path.append(downRightZahyo)
        resultList.append(search(path))
        path.pop()
    return resultList

# 各最大値座標から探索
resultList = []
for maxZahyo in maxNumberZahyoList:
    currentPath = [maxZahyo]
    resultList.extend(search(currentPath))

print(resultList)