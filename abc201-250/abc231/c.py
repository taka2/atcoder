# -*- coding: utf-8 -*-
import bisect

N,Q = map(int, input().split())
A = list(map(int, input().split()))
x = []
for i in range(Q):
    x.append(int(input()))

sortedA = sorted(A)

for i in range(Q):
    q = x[i]
    ans = bisect.bisect_left(sortedA, q)
    print(N-ans)