# -*- coding: utf-8 -*-
N = int(input())
S = input()

kushi = False
streak = 0
ans = -1

for i in range(N):
    if S[i] == '-':
        if streak > 0:
            ans = max(ans, streak)
        kushi = True
        streak = 0
    else:
        streak += 1
        if kushi:
            ans = max(ans, streak)

print(ans)