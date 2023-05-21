# -*- coding: utf-8 -*-
import bisect

N,M,D = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
sortedA = sorted(A)
sortedB = sorted(B)

ans = -1
indexA = len(A)-1
indexB = len(B)-1
while indexA >= 0 and indexB >= 0:
    valueA = sortedA[indexA]
    valueB = sortedB[indexB]
    if abs(valueA-valueB) <= D:
        ans = valueA + valueB
        break
    if valueA < valueB:
        indexB -= 1
    else:
        indexA -= 1

print(ans)