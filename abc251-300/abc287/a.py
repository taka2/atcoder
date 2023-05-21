# -*- coding: utf-8 -*-
N = int(input())

agree = 0
for i in range(N):
    S = input()
    if S == 'For':
        agree += 1

if (N - agree) <= (N//2):
    print("Yes")
else:
    print("No")
