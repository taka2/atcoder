# -*- coding: utf-8 -*-
A,B,K = map(int, input().split())

ans = []
for i in range(K):
    if A+i <= B:
        ans.append(A+i)

for i in range(K):
    if B-i not in ans:
        if B-i >= A:
            ans.append(B-i)

sortedAns = sorted(ans)
for i in range(len(sortedAns)):
    print(sortedAns[i])