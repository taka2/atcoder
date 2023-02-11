# -*- coding: utf-8 -*-
N,M = map(int, input().split())
A = list(map(int, input().split()))
mapA = {}
for i in range(M):
    mapA[A[i]] = 1

ans = []
stack = []
for i in range(1, N+1):
    # レ点がある場合
    if i in mapA:
        # スタックに積む
        stack.append(i)
    else:
        ans.append(i)
        for j in range(len(stack)-1, -1, -1):
            ans.append(stack[j])
        stack = []

print(*ans)