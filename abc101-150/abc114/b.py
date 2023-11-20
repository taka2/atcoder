# -*- coding: utf-8 -*-
S = input()

ans = 1000
for i in range(len(S)-2):
    X = int(S[i] + S[i+1] + S[i+2])
    ans = min(ans, abs(753-int(X)))

print(ans)