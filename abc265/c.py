# -*- coding: utf-8 -*-
h,w = map(int, input().split())

grid = []
for i in range(h):
    grid.append(input())

pos = (0,0)
movedPosition = {}
while True:
    operation = grid[pos[0]][pos[1]]
    if operation == 'U':
        if pos[0] == 0:
            break
        else:
            pos = (pos[0]-1, pos[1])
    if operation == 'D':
        if pos[0] == h-1:
            break
        else:
            pos = (pos[0]+1, pos[1])
    if operation == 'L':
        if pos[1] == 0:
            break
        else:
            pos = (pos[0], pos[1]-1)
    if operation == 'R':
        if pos[1] == w-1:
            break
        else:
            pos = (pos[0], pos[1]+1)
    if (pos[0], pos[1]) in movedPosition:
        print("-1")
        exit(0)
    movedPosition[(pos[0], pos[1])] = 1

print(pos[0]+1, pos[1]+1)
