# -*- coding: utf-8 -*-
S = input()
T = input()

ans = False
for i in range(len(S)):
    Sdash = S[i:] + S[:i]
    if Sdash == T:
        ans = True
    
if ans:
    print("Yes")
else:
    print("No")