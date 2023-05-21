# -*- coding: utf-8 -*-
R,C = map(int, input().split())
B = []
for i in range(R):
    row = input()
    B.append(row)

Blasted = []
for i in range(R):
    Blasted.append([False]*C)

for i in range(R):
    for j in range(C):
        if B[i][j].isdigit():
            power = int(B[i][j])
            for ii in range(R):
                for jj in range(C):
                    distance = abs(i-ii) + abs(j-jj)
                    if distance <= power:
                        Blasted[ii][jj] = True

for i in range(R):
    s = ""
    for j in range(C):
        if Blasted[i][j]:
            s += "."
        else:
            s += B[i][j]
    print(s)
    