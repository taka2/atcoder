# -*- coding: utf-8 -*-
N = int(input())
S = input()

ans = ""
for i in range(len(S)):
    ans += chr(((ord(S[i])-65+N) % 26) + 65)

print(ans)