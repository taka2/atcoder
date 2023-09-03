# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))

ans = True
for i in range(N):
    if A[i] % 2 == 0:
        if A[i] % 3 != 0 and A[i] % 5 != 0:
            ans = False
            break

if ans:
    print("APPROVED")
else:
    print("DENIED")