# -*- coding: utf-8 -*-
N = int(input())
S = input()
T = input()

ans = True
for i in range(N):
    Si = S[i]
    Ti = T[i]
    if Si == Ti or (Si=='1' and Ti=='l') or (Si=='l' and Ti=='1') or (Si=='0' and Ti=='o') or (Si=='o' and Ti=='0'):
        continue
    else:
        ans = False
        break

if ans:
    print("Yes")
else:
    print("No")