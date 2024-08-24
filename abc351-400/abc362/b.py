# -*- coding: utf-8 -*-
XA,YA = map(int, input().split())
XB,YB = map(int, input().split())
XC,YC = map(int, input().split())

AB2 = (XA-XB)**2 + (YA-YB)**2
BC2 = (XB-XC)**2 + (YB-YC)**2
CA2 = (XC-XA)**2 + (YC-YA)**2

if AB2 + BC2 == CA2 or BC2 + CA2 == AB2 or CA2 + AB2 == BC2:
    print("Yes")
else:
    print("No")