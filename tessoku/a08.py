# -*- coding: utf-8 -*-
H,W = map(int, input().split())
X = []
for i in range(H):
    X.append(list(map(int, input().split())))

# 横方向の累積和
Xsum = [[0] * (W+1)]
for i in range(H):
    sum = 0
    row = [0]
    for j in range(W):
        sum += X[i][j]
        row.append(sum)
    Xsum.append(row)

# 縦方向の累積和
for i in range(H+1):
    for j in range(W+1):
        if i != 0:
            Xsum[i][j] += Xsum[i-1][j]

Q = int(input())
for i in range(Q):
    A,B,C,D = map(int, input().split())
    print(Xsum[C][D] + Xsum[A-1][B-1] - Xsum[A-1][D] - Xsum[C][B-1])