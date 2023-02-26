# -*- coding: utf-8 -*-
N = int(input())
AB = []
for i in range(N):
    a,b = map(int, input().split())
    AB.append((a,b))

prev = (-1,-1)
ans = 2**N
mod = 998244353
for i in range(N):
    (a,b) = AB[i]
    if prev[0] == a or prev[1] == a or prev[0] == b or prev[1] == b:
        ans -= N
    prev = (a,b)

print(ans % mod)