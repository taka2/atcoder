# -*- coding: utf-8 -*-
H,W = map(int, input().split())
Si, Sj = map(int, input().split())
C = []
for i in range(H):
    row = list(input())
    C.append(row)
X = input()

currentY = Si-1
currentX = Sj-1

for i in range(len(X)):
    if X[i] == 'L':
        if currentX == 0:
            pass
        elif C[currentY][currentX-1] == '#':
            pass
        else:
            currentX -= 1
    if X[i] == 'R':
        if currentX == (W-1):
            pass
        elif C[currentY][currentX+1] == '#':
            pass
        else:
            currentX += 1
    if X[i] == 'U':
        if currentY == 0:
            pass
        elif C[currentY-1][currentX] == '#':
            pass
        else:
            currentY -= 1
    if X[i] == 'D':
        if currentY == (H-1):
            pass
        elif C[currentY+1][currentX] == '#':
            pass
        else:
            currentY += 1

print(currentY+1,currentX+1)