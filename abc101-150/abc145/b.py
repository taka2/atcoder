# -*- coding: utf-8 -*-
N = int(input())
S = input()

if N % 2 == 1:
    print("No")
elif S[0:N//2] == S[N//2:]:
    print("Yes")
else:
    print("No")
