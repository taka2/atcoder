# -*- coding: utf-8 -*-
S = input()
T = input()

def hantei(a, b):
    if a == '?' or b == '?' or a == b:
        return True
    else:
        return False

pre = [True]
suf = [True]

preMatch = True
for i in range(len(T)):
    if preMatch and hantei(S[i], T[i]):
        pass
    else:
        preMatch = False
    pre.append(preMatch)

reverseS = S[::-1]
reverseT = T[::-1]

sufMatch = True
for i in range(len(T)):
    if sufMatch and hantei(reverseS[i], reverseT[i]):
        pass
    else:
        sufMatch = False
    suf.append(sufMatch)

for x in range(len(T)+1):
    preLength = x
    sufLength = len(T) - x
    if pre[preLength] and suf[sufLength]:
        print("Yes")
    else:
        print("No")