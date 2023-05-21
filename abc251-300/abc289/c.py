# -*- coding: utf-8 -*-
import itertools

N,M = map(int, input().split())
S = []
for i in range(M):
    C = int(input())
    A = list(map(int, input().split()))
    S.append(A)

ans = 0
for i in range(1, M+1):
    for j in itertools.combinations(S, i):
        judgeArray = [0] * (N+1)
        for k in j:
            for l in k:
                judgeArray[l] = 1
    
        judge = True
        for i in range(1, N+1):
            if judgeArray[i] == 0:
                judge = False
                break
        if judge:
            ans += 1

print(ans)