# -*- coding: utf-8 -*-
s = input()
stIndex = -1
ans = -1
for i in range(len(s)):
    if stIndex == -1 and s[i] == 'A':
        stIndex = i
    elif stIndex != -1 and s[i] == 'Z':
        ans = max(ans, i-stIndex+1)

print(ans)