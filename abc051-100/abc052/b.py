# -*- coding: utf-8 -*-
N = int(input())
S = input()

x = 0
ans = 0

for i in range(N):
    if S[i] == 'I':
        x += 1
        ans = max(x, ans)
    else:
        x -= 1

print(ans)