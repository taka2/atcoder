# -*- coding: utf-8 -*-
S = input()
flag = False
ans = ""
for i in range(len(S)):
    if S[i] == '|' and not flag:
        flag = True
        continue
    elif S[i] == '|' and flag:
        flag = False
        continue
    elif not flag:
        ans += S[i]

print(ans)