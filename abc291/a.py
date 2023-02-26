# -*- coding: utf-8 -*-
S = input()

for i in range(len(S)):
    if S[i] >= 'A' and S[i] <= 'Z':
        print(i+1)
        break