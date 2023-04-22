# -*- coding: utf-8 -*-
N = int(input())
S = input()

flag = False
jewel = False
ans = False
for i in range(N):
    if S[i] == '|' and not flag:
        flag = True
    if S[i] == '*' and flag:
        jewel = True
    if S[i] == '|' and jewel and flag:
        ans = True

if ans:
    print("in")
else:
    print("out")