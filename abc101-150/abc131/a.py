# -*- coding: utf-8 -*-
S = input()

prev = ""
ans = True
for i in range(len(S)):
    if prev == S[i]:
        ans = False
        break
    prev = S[i]

if ans:
    print("Good")
else:
    print("Bad")