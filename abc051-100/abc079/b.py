# -*- coding: utf-8 -*-
N = int(input())
L = []
L.append(2)
L.append(1)
for i in range(2, 87):
    L.append(L[i-1] + L[i-2])

print(L[N])