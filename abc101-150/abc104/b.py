# -*- coding: utf-8 -*-
S = input()

condition1 = S[0] == 'A'

largeCCount = 0
for i in range(2, len(S)-1):
    if S[i] == 'C':
        largeCCount += 1

if S[0] == 'C' or S[1] == 'C' or S[-1] == 'C':
    condition2 = False
elif largeCCount == 1:
    condition2 = True
else:
    condition2 = False

largeCount = 0
for i in range(len(S)):
    if S[i] >= 'A' and S[i] <= 'Z':
        largeCount += 1

condition3 = False
if largeCount == 2:
    condition3 = True
    

if condition1 and condition2 and condition3:
    print("AC")
else:
    print("WA")