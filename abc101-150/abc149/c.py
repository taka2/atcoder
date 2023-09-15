# -*- coding: utf-8 -*-
import math
X = int(input())

MAX = 10**5+9

prime = [True] * (MAX)
for i in range(2, int(math.sqrt(MAX))+1):
    if prime[i]:
        for i in range(i*2,MAX,i):
            prime[i] = False

for i in range(X,MAX):
    if prime[i]:
        print(i)
        break