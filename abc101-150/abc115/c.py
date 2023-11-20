# -*- coding: utf-8 -*-
N,K = map(int, input().split())

h = []
for i in range(N):
    h.append(int(input()))

sortedH = sorted(h)

diff = []
for i in range(N-1):
    diff.append(sortedH[i+1] - sortedH[i])

sortedDiff = sorted(diff)

ans = 0
for i in range(K-1):
    ans += sortedDiff[i]

print(ans)