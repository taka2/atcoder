# -*- coding: utf-8 -*-
N,L = map(int, input().split())

ans = 0
for i in range(N):
    A,B = input().split()
    A = int(A)
    if B == 'E':
        ans = max(ans, L-A)
    else:
        ans = max(ans, A)

print(ans)