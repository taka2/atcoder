# -*- coding: utf-8 -*-
T = int(input())
N = int(input())
zenjitsuhi = []
for i in range(T+1):
    zenjitsuhi.append(0)

for i in range(N):
    L,R = map(int, input().split())
    zenjitsuhi[L] += 1
    zenjitsuhi[R] -= 1

sum = 0
for i in range(T):
    sum += zenjitsuhi[i]
    print(sum)
