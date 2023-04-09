# -*- coding: utf-8 -*-
N,K = map(int, input().split())
S = input()

countON = 0
for i in range(len(S)):
    if S[i] == '1':
        countON += 1

if K % 2 == 0 and countON % 2 == 0:
    print("Yes")
elif K % 2 == 1 and countON % 2 == 1:
    print("Yes")
else:
    print("No")