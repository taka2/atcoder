# -*- coding: utf-8 -*-
S = input()

zeroCount = 0
oneCount = 0
for i in range(len(S)):
    if S[i] == '0':
        zeroCount += 1
    else:
        oneCount += 1

print(min(zeroCount, oneCount) * 2)