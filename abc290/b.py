# -*- coding: utf-8 -*-
N,K = map(int, input().split())
S = input()

sum = 0
T = ""
for i in range(N):
    if S[i] == 'o':
        sum += 1

    if sum > K:
        T += "x"
    else:
        T += S[i]

print(T)