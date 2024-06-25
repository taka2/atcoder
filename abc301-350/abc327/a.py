# -*- coding: utf-8 -*-
N = int(input())
S = input()

prev = ""
flag = False
for i in range(N):
    if prev == 'a' and S[i] == 'b':
        flag = True
        break
    elif prev == 'b' and S[i] == 'a':
        flag = True
        break
    prev = S[i]

if flag:
    print("Yes")
else:
    print("No")