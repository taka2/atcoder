# -*- coding: utf-8 -*-
from collections import deque

MOD = 998244353

Q = int(input())

S = deque([1])
ans = 1

for i in range(Q):
    query = input().split()
    if query[0] == '1':
        x = int(query[1])
        ans = (ans * 10 + x) % MOD
        S.append(x)
    elif query[0] == '2':
        t = S.popleft()
        keta = pow(10, len(S), MOD)
        ans -= t*keta
        ans %= MOD
    elif query[0] == '3':
        print(ans % MOD)