# -*- coding: utf-8 -*-
K,X = map(int, input().split())

fr = max(X-K+1, -1000000)
to = min(X+K-1, 1000000)

ans = []
for i in range(fr,to+1):
    ans.append(i)

print(*ans)