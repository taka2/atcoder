# -*- coding: utf-8 -*-
H,W = map(int, input().split())
S = []
for i in range(H):
    S.append(input())

minLeft = W-1
maxRight = 0
minTop = H-1
maxBottom = 0

for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            minLeft = min(minLeft, j)
            maxRight = max(maxRight, j)
            minTop = min(minTop, i)
            maxBottom = max(maxBottom, i)

for i in range(H):
    for j in range(W):
        if S[i][j] == '.' and i>=minTop and i<=maxBottom and j>=minLeft and j<=maxRight:
            print(i+1,j+1)
            exit(0)