# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))

ans = A[0]
if 0 in A:
    ans = 0
else:
    for i in range(1,N):
        ans *= A[i]
        if ans > 10**18:
            ans = -1
            break

print(ans)