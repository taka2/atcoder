# -*- coding: utf-8 -*-
N = int(input())
K = int(input())

tmp = 1
for i in range(N):
    tmp1 = tmp * 2
    tmp2 = tmp + K
    tmp = min(tmp1, tmp2)

print(tmp)