# -*- coding: utf-8 -*-
import math

N = int(input())
sqrtN = int(math.sqrt(N))

ans = []
for i in range(1,sqrtN+1):
    if N % i == 0:
        ans.append(i)
        if N // i != i:
            ans.append(N//i)

sortedAns = sorted(ans)
for i in range(len(ans)):
    print(sortedAns[i])