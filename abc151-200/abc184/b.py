# -*- coding: utf-8 -*-
N,X = map(int, input().split())
S = input()

current = X
for i in range(N):
    if S[i] == 'o':
        current += 1
    else:
        if current > 0:
            current -= 1

print(current)