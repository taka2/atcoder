# -*- coding: utf-8 -*-
S = input()
countMap = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0}

for i in range(len(S)):
    countMap[S[i]] += 1

print(countMap['A'], countMap['B'], countMap['C'], countMap['D'], countMap['E'], countMap['F'])