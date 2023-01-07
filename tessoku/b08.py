# -*- coding: utf-8 -*-
N = int(input())
XY = []
for i in range(N):
    X,Y = map(int, input().split())
    XY.append((X,Y))

H = 1500
W = 1500

# 0で埋めた二次元配列を用意する
X = []
for i in range(H):
    row = []
    for j in range(W):
        row.append(0)
    X.append(row)

# 指定されたXY座標に1をセット
for i in range(N):
    x = XY[i][0]
    y = XY[i][1]
    X[y-1][x-1] = 1

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
    print(Xsum[D][C] + Xsum[B-1][A-1] - Xsum[D][A-1] - Xsum[B-1][C])