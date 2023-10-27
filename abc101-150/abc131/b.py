# -*- coding: utf-8 -*-
N,L = map(int, input().split())

ans = 0
if L > 0:
    for i in range(N-1):
        ans += L+i+1
else:
    if N+L > 0:
        for i in range(N):
            ans += L+i
    else:
        for i in range(N-1):
            ans += L+i

print(ans)