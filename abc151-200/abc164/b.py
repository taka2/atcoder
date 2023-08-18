# -*- coding: utf-8 -*-
A,B,C,D = map(int, input().split())

turn = "T"
ans = ""
while A>0 and C>0:
    if turn == "T":
        C -= B
        if C <= 0:
            ans = "T"
            break
        turn = "A"
    else:
        A -= D
        if A <= 0:
            ans = "A"
            break
        turn = "T"

if ans == "T":
    print("Yes")
else:
    print("No")