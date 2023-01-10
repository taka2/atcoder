# -*- coding: utf-8 -*-
H,W,N = map(int, input().split())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))

# 0初期化
X = []
for i in range(H+1):
    row = []
    for j in range(W+1):
        row.append(0)
    X.append(row)

# 雪を降らせる
for i in range(N):
    x1 = A[i][0] - 1
    y1 = A[i][1] - 1
    x2 = A[i][2] - 1
    y2 = A[i][3] - 1
    X[x2+1][y2+1] += 1
    X[x1][y1] += 1
    X[x2+1][y1] -= 1
    X[x1][y2+1] -= 1

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

for i in range(1,H+1):
    row = Xsum[i][1:]
    print(" ".join(map(str, row)))