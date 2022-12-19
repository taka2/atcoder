# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))

for i in range(N):
    A[i] -= 1

same = 0
for i in range(N):
    if A[i] == i:
        same += 1
ans = (same * (same-1)) // 2

for i in range(N):
    j = A[i]
    if i < j and A[j] == i:
        ans += 1
    
print(ans)