# -*- coding: utf-8 -*-
V,A,B,C = map(int, input().split())

while V>=0:
    if V-A <0:
        print("F")
        break
    V -= A
    if V-B <0:
        print("M")
        break
    V -= B
    if V-C <0:
        print("T")
        break
    V -= C
