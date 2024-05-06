# -*- coding: utf-8 -*-
H,W = map(int, input().split())
S = []
for i in range(H):
    S.append(input())

eightdirection = [[-1,-1], [0,-1], [1,-1], [-1, 0], [1,0], [-1, 1], [0, 1], [1,1]]

for i in range(H):
    line = ""
    for j in range(W):
        if S[i][j] == '#':
            line += '#'
        else:
            bombs = 0
            for k in eightdirection:
                x = j + k[0]
                y = i + k[1]
                if x < 0 or y < 0 or x >= W or y >= H:
                    continue
                else:
                    if S[y][x] == '#':
                        bombs += 1
            line += str(bombs)
    print(line)