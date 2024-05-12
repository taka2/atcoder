# -*- coding: utf-8 -*-
N = int(input())
d = []
for i in range(N):
    d.append(int(input()))

sortedD = sorted(d)

ans = 0
prev = -1
for i in range(N):
    if sortedD[i] > prev:
        ans += 1
    prev = sortedD[i]

print(ans)