# -*- coding: utf-8 -*-
N,P,Q,R,S = map(int, input().split())
A = list(map(int, input().split()))

LEFT = A[:P-1]
PQ = A[P-1:Q]
MID = A[Q:R-1]
RS = A[R-1:S]
RIGHT = A[S:]

B = LEFT
B.extend(RS)
B.extend(MID)
B.extend(PQ)
B.extend(RIGHT)
print(" ".join(map(str, B)))