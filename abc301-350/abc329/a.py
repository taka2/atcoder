# -*- coding: utf-8 -*-
S = input()

ans = S[0]
for i in range(len(S)-1):
    ans += " " + S[i+1]

print(ans)