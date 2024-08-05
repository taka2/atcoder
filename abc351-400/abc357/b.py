# -*- coding: utf-8 -*-
S = input()

small = 0
large = 0
for i in range(len(S)):
    if S[i] >= 'a' and S[i] <= 'z':
        small += 1
    else:
        large += 1

if small > large:
    print(S.lower())
else:
    print(S.upper())