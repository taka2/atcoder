# -*- coding: utf-8 -*-
N = input()
ans = False
for i in range(len(N)):
    if N[i] == '7':
        ans = True
        break

if ans:
    print("Yes")
else:
    print("No")