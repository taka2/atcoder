# -*- coding: utf-8 -*-
N,K = map(int, input().split())
mapAB = {}
for i in range(N):
    (A,B) = map(int, input().split())
    if A in mapAB:
        mapAB[A] += B
    else:
        mapAB[A] = B

AB = []
for A in sorted(mapAB):
    AB.append((A,mapAB[A]))

money = K
pos = 0
for i in range(len(AB)):
    (A,B) = AB[i]
    if money >= (A-pos):
        pos += A
        money = money - A + B
    else:
        pos += money
        money = 0
        break

pos += money
print(pos)