# -*- coding: utf-8 -*-
N = int(input())
poems = [(0,0)]
for i in range(N):
    S,T = input().split()
    poems.append((S, int(T)))

submitted = {}
maxScore = 0
maxScoreIndex = 0

for i in range(1, N+1):
    (S,T) = poems[i]
    if S not in submitted:
        submitted[S] = 1
        if T > maxScore:
            maxScore = T
            maxScoreIndex = i

print(maxScoreIndex)