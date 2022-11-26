# -*- coding: utf-8 -*-
# 整数の入力
S = input()

count = 0
for i in (range(len(S))):
    if S[i] == 'v':
        count += 1
    elif S[i] == 'w':
        count += 2

print(count)