# -*- coding: utf-8 -*-
import math

K = int(input())

ans = 0
for i in range(1,K+1):
    for j in range(1,K+1):
        for k in range(1,K+1):
            gcdtmp = math.gcd(i,j)
            ans += math.gcd(gcdtmp, k)

print(ans)