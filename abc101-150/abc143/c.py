# -*- coding: utf-8 -*-
N = int(input())
S = input()

ans = 0
prev = ""
for i in range(N):
    if S[i] != prev:
        ans += 1
    prev = S[i]

print(ans)