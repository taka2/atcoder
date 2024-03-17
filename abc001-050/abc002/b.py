# -*- coding: utf-8 -*-
W = input()
ans = ""
for i in range(len(W)):
    if W[i] in "aiueo":
        pass
    else:
        ans += W[i]

print(ans)