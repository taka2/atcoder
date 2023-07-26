# -*- coding: utf-8 -*-
S = input()

komoji = "abcdefghijklmnopqrstuvwxyz"

ans = True
for i in range(len(S)):
    ch = S[i]
    if i % 2 == 0:
        # 奇数
        if ch not in komoji:
            ans = False
            break
    else:
        # 偶数
        if ch in komoji:
            ans = False
            break

if ans:
    print("Yes")
else:
    print("No")