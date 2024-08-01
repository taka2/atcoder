# -*- coding: utf-8 -*-
N = int(input())
S = []
for i in range(N):
    S.append(input())

prev = ""
ans = True
for i in range(N):
    if prev == "sweet" and S[i] == "sweet" and i != (N-1):
        ans = False
        break
    prev = S[i]

if ans:
    print("Yes")
else:
    print("No")