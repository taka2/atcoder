# -*- coding: utf-8 -*-
S = input()

checkMap = {}
oomoji = False
komoji = False
daburi = False
for i in range(len(S)):
    if S[i] in checkMap:
        daburi = True
        break
    else:
        checkMap[S[i]] = 1

    if S[i] >= 'A' and S[i] <= 'Z':
        oomoji = True
    elif S[i] >= 'a' and S[i] <= 'z':
        komoji = True

if (not daburi) and oomoji and komoji:
    print("Yes")
else:
    print("No")