# -*- coding: utf-8 -*-
import math

N,D = map(int, input().split())
X = []
for i in range(N):
    Xn = list(map(int, input().split()))
    X.append(Xn)

ans = 0
for i in range(N):
    for j in range(i+1, N):
        Xy = X[i]
        Xz = X[j]
        distsum = 0
        for k in range(D):
            distsum += (Xy[k] - Xz[k]) ** 2
        dist = math.sqrt(distsum)

        if dist == int(dist):
            ans += 1

print(ans)