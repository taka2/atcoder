# -*- coding: utf-8 -*-
A,B = map(int, input().split())
mapA = {}
mapA[A] = 1
mapA[B] = 1

if 1 in mapA and 2 in mapA:
    print("3")
elif 1 in mapA and 3 in mapA:
    print("2")
elif 2 in mapA and 3 in mapA:
    print("1")
else:
    print("-1")