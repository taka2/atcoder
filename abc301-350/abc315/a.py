# -*- coding: utf-8 -*-
S = input()

ans = ""
for i in range(len(S)):
    if S[i] not in "aiueo":
        ans += S[i]

print(ans)