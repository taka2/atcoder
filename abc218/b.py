# -*- coding: utf-8 -*-
P = list(map(int, input().split()))
S = " abcdefghijklmnopqrstuvwxyz"

ans = ""
for p in P:
    ans += S[p]

print(ans)