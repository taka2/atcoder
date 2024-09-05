# -*- coding: utf-8 -*-
A,B,C = map(int, input().split())

if C>B:
    if A<B or A>C:
        print("Yes")
    else:
        print("No")
else:
    if A<B and A>C:
        print("Yes")
    else:
        print("No")