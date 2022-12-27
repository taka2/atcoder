# -*- coding: utf-8 -*-
S = input()
T = input()

sindex = 0
for i in range(len(T)):
    if sindex == len(S) or S[sindex] != T[i]:
        if sindex >= 2 and S[sindex-1] == T[i] and S[sindex-2] == T[i]:
            # OK
            pass
        else:
            # NG
            sindex = -1
            break
    else:
        # OK
        sindex += 1

if sindex == -1 or sindex != len(S):
    print("No")
else:
    print("Yes")