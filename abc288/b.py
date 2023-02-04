# -*- coding: utf-8 -*-
N,K = map(int, input().split())
S = []
for i in range(N):
    S.append(input())

ranked = sorted(S[:K])
for i in range(len(ranked)):
    print(ranked[i])