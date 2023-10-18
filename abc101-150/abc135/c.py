# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for i in range(N-1,-1,-1):
    if B[i] > A[i+1]:
        plus = A[i+1]
        zan = B[i] - A[i+1]
        A[i+1] = 0
        add = min(zan, A[i])
        A[i] -= add
        ans += (plus + add)
    else:
        A[i+1] -= B[i]
        ans += B[i]

print(ans)