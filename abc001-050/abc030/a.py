# -*- coding: utf-8 -*-
A,B,C,D = map(int, input().split())

if B*C == A*D:
    print("DRAW")
elif B*C > A*D:
    print("TAKAHASHI")
else:
    print("AOKI")