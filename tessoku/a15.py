# -*- coding: utf-8 -*-
import bisect

N = int(input())
A = list(map(int, input().split()))

setA = set(A)
sortedListA = sorted(list(setA))

B = []
for i in range(N):
    B.append(bisect.bisect(sortedListA, A[i]))

print(*B)