# -*- coding: utf-8 -*-
H,W = map(int, input().split())
A = []
for i in range(H):
    A.append(list(map(int, input().split())))

for i in range(W):
    list = []
    for j in range(H):
        list.append(A[j][i])

    print(*list)