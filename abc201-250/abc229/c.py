# -*- coding: utf-8 -*-
N,W = map(int, input().split())
AB = []
for i in range(N):
    A,B = map(int, input().split())
    AB.append((A,B))

sortedAB = sorted(AB, reverse=True)

value = 0
weight = 0
for i in range(N):
    (A,B) = sortedAB[i]
    if (weight + B) >= W:
        value += (W-weight) * A
        break
    else:
        value += (A*B)
        weight += B

print(value)