# -*- coding: utf-8 -*-
N = int(input())

list = []
for i in range(N):
    row = []
    for j in range(i+1):
        if j == 0:
            row.append(1)
        elif j == i:
            row.append(1)
        else:
            row.append(list[i-1][j-1] + list[i-1][j])
    list.append(row)
    print(" ".join(map(str, row)))