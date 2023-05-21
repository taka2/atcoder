# -*- coding: utf-8 -*-
H,W = map(int, input().split())

points = []
for i in range(H):
    S = input()
    if 'o' in S:
        for j in range(W):
            if S[j] == 'o':
                points.append((i,j))

distance = abs(points[0][0] - points[1][0]) + abs(points[0][1] - points[1][1])
print(distance)