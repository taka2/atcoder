# -*- coding: utf-8 -*-
S = input()
ans = ""
for i in range(len(S)):
    if i == 0:
        ans += S[i].upper()
    else:
        ans += S[i].lower()

print(ans)