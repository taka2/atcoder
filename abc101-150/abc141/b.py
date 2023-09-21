# -*- coding: utf-8 -*-
S = input()

ans = True
for i in range(len(S)):
    if i % 2 == 0:
        # 奇数
        if S[i] == 'L':
            ans = False
            break
    else:
        # 偶数
        if S[i] == 'R':
            ans = False
            break

if ans:
    print("Yes")
else:
    print("No")