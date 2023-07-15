# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))

cutted = [False] * 360

curpos = 0
cutted[0] = True
for i in range(N):
    curpos = (curpos-A[i]+360) % 360
    cutted[curpos] = True

maxAngle = 0
prevAngle = 0
for i in range(360):
    if cutted[i]:
        maxAngle = max(maxAngle, i-prevAngle)
        prevAngle = i

maxAngle = max(maxAngle, 360-prevAngle)
print(maxAngle)