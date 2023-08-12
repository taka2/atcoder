# -*- coding: utf-8 -*-
S = input()

ans = 0
len = 0
for i in range(3):
    Si = S[i]
    if Si == 'R':
        len += 1
    else:
        ans = max(ans, len)
        len = 0
ans = max(ans, len)

print(ans)