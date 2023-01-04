# -*- coding: utf-8 -*-
N,K = map(int, input().split())

count = 0
for i in range(1,N+1):
    for j in range(1,N+1):
        k = K-i-j
        if k > 0 and k <= N:
            count += 1

print(count)