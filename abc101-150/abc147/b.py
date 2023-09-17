# -*- coding: utf-8 -*-
S = input()

ans = 0
lenS = len(S)
for i in range(lenS//2):
    if S[i] != S[lenS-1-i]:
        ans += 1

print(ans)