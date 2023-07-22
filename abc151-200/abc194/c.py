# -*- coding: utf-8 -*-
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
aggA = defaultdict(int)
for i in range(N):
    aggA[A[i]] += 1

keys = [0] + list(aggA)
ans = 0
for i in range(2, len(keys)):
    for j in range(1, i):
        Ai = keys[i]
        AiCount = aggA[Ai]
        Aj = keys[j]
        AjCOunt = aggA[Aj]
        ans += AiCount * AjCOunt * (Ai-Aj)**2

print(ans)