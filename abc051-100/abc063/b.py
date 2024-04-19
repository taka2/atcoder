# -*- coding: utf-8 -*-
S = input()

mapS = {}
ans = True
for i in range(len(S)):
    if S[i] in mapS:
        ans = False
        break
    else:
        mapS[S[i]] = 1

if ans:
    print("yes")
else:
    print("no")