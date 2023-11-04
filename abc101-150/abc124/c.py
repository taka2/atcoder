# -*- coding: utf-8 -*-
S = input()

ans = 0
current = S[0]
for i in range(1,len(S)):
    if S[i] != current:
        current = S[i]
    else:
        ans += 1
        if current == '0':
            current = '1'
        else:
            current = '0'

print(ans)