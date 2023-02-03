# -*- coding: utf-8 -*-
N = int(input())
T = input()

direction = 'E'
currentPos = (0,0)

for i in range(N):
    if T[i] == 'R':
        if direction == 'E':
            direction = 'S'
        elif direction == 'S':
            direction = 'W'
        elif direction == 'W':
            direction = 'N'
        elif direction == 'N':
            direction = 'E'
    else:
        if direction == 'E':
            currentPos = (currentPos[0]+1, currentPos[1])
        elif direction == 'S':
            currentPos = (currentPos[0], currentPos[1]-1)
        elif direction == 'W':
            currentPos = (currentPos[0]-1, currentPos[1])
        elif direction == 'N':
            currentPos = (currentPos[0], currentPos[1]+1)

print(*currentPos)