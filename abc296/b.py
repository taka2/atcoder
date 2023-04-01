# -*- coding: utf-8 -*-
S = []
for i in range(8):
    S.append(input())

for i in range(8):
    for j in range(8):
        if S[i][j] == '*':
            row = str(8-i)
            column = "abcdefgh"[j]
            print(column + row)
            break