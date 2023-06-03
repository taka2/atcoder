# -*- coding: utf-8 -*-
W,H = map(int, input().split())
N = int(input())
pq = []
for i in range(N):
    (p,q) = map(int, input().split())
    pq.append((p,q))

A = int(input())
a = list(map(int, input().split())) + [W]
B = int(input())
b = list(map(int, input().split())) + [H]

sum = [[0] * (A+1) for i in range(B+1)]
for x in range(A+1):
    for y in range(B+1):
        for n in range(N):
            if x == 0:
                prelinex = 0
            else:
                prelinex = a[x-1]
            if y == 0:
                preliney = 0
            else:
                preliney = b[y-1]
            linex = a[x]
            liney = b[y]
            (p,q) = pq[n]
            if p > prelinex and p < linex and q > preliney and q < liney:
                sum[y][x] += 1

minvalue = N
maxvalue = 0
for x in range(A+1):
    for y in range(B+1):
        minvalue = min(minvalue, sum[x][y])
        maxvalue = max(maxvalue, sum[x][y])

print(minvalue, maxvalue)