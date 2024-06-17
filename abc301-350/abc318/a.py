# -*- coding: utf-8 -*-
N,M,P = map(int, input().split())

ans = 0
current = M
while current <= N:
    current += P
    ans += 1

print(ans)
