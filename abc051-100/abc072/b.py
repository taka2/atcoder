# -*- coding: utf-8 -*-
s = input()

ans = ""
for i in range(len(s)):
    if i % 2 == 0:
        ans += s[i]

print(ans)