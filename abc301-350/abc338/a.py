# -*- coding: utf-8 -*-
S = input()
S1 = S.lower()
S2 = S1[0].upper() + S1[1:]

if S == S2:
    print("Yes")
else:
    print("No")