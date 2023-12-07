# -*- coding: utf-8 -*-
A = list(map(int, input().split()))

sortedA = sorted(A)

ans = (sortedA[1]-sortedA[0]) + (sortedA[2]-sortedA[1])
print(ans)