# -*- coding: utf-8 -*-
A,B,C,D,E,F,X = map(int, input().split())

tCycle = X // (A+C)
tAmari = X - tCycle * (A+C)
if tAmari >= A:
    tAmari = A
tMeter = tCycle * A * B + tAmari * B

aCycle = X // (D+F)
aAmari = X - aCycle * (D+F)
if aAmari >= D:
    aAmari = D
aMeter = aCycle * D * E + aAmari * E

if tMeter > aMeter:
    print("Takahashi")
elif aMeter > tMeter:
    print("Aoki")
else:
    print("Draw")