# -*- coding: utf-8 -*-
A,B,K = map(int, input().split())

ansA = 0
if K>=A:
    ansA = 0
else:
    ansA = A-K

ansB = B
if ansA == 0:
    if (K-A)>=B:
        ansB = 0
    else:
        ansB = B - (K-A)

print(ansA,ansB)