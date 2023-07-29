# -*- coding: utf-8 -*-
S = input()

questionMarkCount = 0
for i in range(len(S)):
    if S[i] == '?':
        questionMarkCount += 1