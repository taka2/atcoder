# -*- coding: utf-8 -*-
S = input()
B1 = -1
B2 = -1
K = -1
R1 = -1
R2 = -1

for i in range(len(S)):
    if S[i] == 'B':
        if B1 == -1:
            B1 = i
        else:
            B2 = i
    elif S[i] == 'K':
        K = i
    elif S[i] == 'R':
        if R1 == -1:
            R1 = i
        else:
            R2 = i

if (B1 % 2 != B2 % 2) and R1 < K and K < R2:
    print("Yes")
else:
    print("No")