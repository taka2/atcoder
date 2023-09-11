# -*- coding: utf-8 -*-
C = input()
S = "abcdefghijklmnopqrstuvwxyz"

for i in range(len(S)):
    if C == S[i]:
        print(S[i+1])
        break