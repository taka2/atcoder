# -*- coding: utf-8 -*-
S = input()
T = input()

ans = len(S)
for offset in range(len(S)-len(T)+1):
    count = 0
    for i in range(len(T)):
        Si = S[offset+i]
        Ti = T[i]
        if Si != Ti:
            count += 1
    ans = min(ans, count)

print(ans)