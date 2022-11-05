# -*- coding: utf-8 -*-
# 整数の入力
s = list(input())

maxIndex = -1
for i in range(len(s)):
    if s[i] == 'a':
        maxIndex = i+1

print(maxIndex)