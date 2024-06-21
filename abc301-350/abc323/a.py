# -*- coding: utf-8 -*-
S = input()

ans = True
for i in range(len(S)):
    if i % 2 == 1 and S[i] == '1':
        ans = False
        break

if ans:
    print("Yes")
else:
    print("No")