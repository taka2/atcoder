# -*- coding: utf-8 -*-
A,B,C,D = map(int, input().split())

left = A+B
right = C+D

if left > right:
    print("Left")
elif right > left:
    print("Right")
else:
    print("Balanced")