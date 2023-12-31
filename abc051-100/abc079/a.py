# -*- coding: utf-8 -*-
N = input()

maxseq = 0
seq = 0
prev = ""

for i in range(len(N)):
    if prev != N[i]:
        maxseq = max(maxseq, seq)
        seq = 1
    else:
        seq += 1
    prev = N[i]
maxseq = max(maxseq, seq)

if maxseq >= 3:
    print("Yes")
else:
    print("No")