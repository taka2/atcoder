# -*- coding: utf-8 -*-
N = int(input())
S = input()

current = S[0]

ans = True
for i in range(1, N):
    if current == S[i]:
        ans = False
        break
    else:
        current = S[i]

if ans:
    print("Yes")
else:
    print("No")