# -*- coding: utf-8 -*-
N = int(input())
p = [0] + list(map(int, input().split()))

Q = [0] * (N+1)
for i in range(1,N+1):
    Q[p[i]] = i

Q.pop(0)
print(*Q)