# -*- coding: utf-8 -*-
N = int(input())
S = input()

ryo = 0
fuka = 0

for i in range(N):
    if S[i] == 'o':
        ryo += 1
    if S[i] == 'x':
        fuka += 1

if ryo > 0 and fuka == 0:
    print("Yes")
else:
    print("No")