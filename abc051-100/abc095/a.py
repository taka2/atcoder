# -*- coding: utf-8 -*-
S = input()

ans = 700
for i in range(len(S)):
    if S[i] == 'o':
        ans += 100

print(ans)