# -*- coding: utf-8 -*-
N = int(input())
ST = []
for i in range(N):
    S,T = input().split()
    ST.append((int(T), S))

sortedST = sorted(ST, reverse=True)
print(sortedST[1][1])