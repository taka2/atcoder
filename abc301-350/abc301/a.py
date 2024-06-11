# -*- coding: utf-8 -*-
N = int(input())
S = input()

countT = 0
countA = 0
for i in range(N):
    if S[i] == 'T':
        countT += 1
    else:
        countA += 1

if countT > countA:
    print("T")
elif countA > countT:
    print("A")
else:
    if S[-1] == 'T':
        print("A")
    else:
        print("T")