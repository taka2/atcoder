# -*- coding: utf-8 -*-
H,W = map(int, input().split())
A = [[0] * (W+1)]
for i in range(H):
    A.append([0] + list(map(int, input().split())))

ans = True
for i1 in range(1,H+1):
    for j1 in range(1,W+1):
        for i2 in range(1,H+1):
            for j2 in range(1,W+1):
                if i2 > i1 and j2 > j1:
                    if (A[i1][j1] + A[i2][j2]) <= (A[i2][j1] + A[i1][j2]):
                        pass
                    else:
                        ans = False
                        break

if ans:
    print("Yes")
else:
    print("No")