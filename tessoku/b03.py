# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))

ans = False
for i in range(N):
    for j in range(1,N):
        for k in range(2,N):
            if i==j or j==k or i==k:
                continue
            sum = A[i]+A[j]+A[k]
            if sum == 1000:
                ans = True
                break
        if ans:
            break
    if ans:
        break

if ans:
    print("Yes")
else:
    print("No")