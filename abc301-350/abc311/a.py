# -*- coding: utf-8 -*-
N = int(input())
S = input()

flagA = False
flagB = False
flagC = False
for i in range(N):
    if S[i] == 'A':
        flagA = True
    elif S[i] == 'B':
        flagB = True
    elif S[i] == 'C':
        flagC = True
    if flagA and flagB and flagC:
        print(i+1)
        break