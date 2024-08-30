# -*- coding: utf-8 -*-
N,M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

merged = []
for i in range(N):
    merged.append(A[i])
for j in range(M):
    merged.append(B[j])

sortedMerged = sorted(merged)

flag = False
ans = False
for i in range(N+M):
    if sortedMerged[i] in A:
        if flag:
            ans = True
            break
        flag = True
    else:
        flag = False

if ans:
    print("Yes")
else:
    print("No")