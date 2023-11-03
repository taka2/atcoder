# -*- coding: utf-8 -*-
S = input()

YY = int(S[:2])
MM = int(S[2:])

YYMM = False
MMYY = False

if MM >= 1 and MM <= 12:
    YYMM = True
if YY >= 1 and YY <= 12:
    MMYY = True

if YYMM and MMYY:
    print("AMBIGUOUS")
elif YYMM:
    print("YYMM")
elif MMYY:
    print("MMYY")
else:
    print("NA")