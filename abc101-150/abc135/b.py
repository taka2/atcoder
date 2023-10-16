# -*- coding: utf-8 -*-
N = int(input())
p = list(map(int, input().split()))

c = list(range(1,N+1))

diff = 0
for i in range(N):
    if p[i] != c[i]:
        diff += 1

if diff >= 3:
    print("NO")
else:
    print("YES")