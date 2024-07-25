# -*- coding: utf-8 -*-
N,M = map(int, input().split())
H = list(map(int, input().split()))

zan = M
ans = 0
for i in range(N):
    if zan >= H[i]:
        ans += 1
    else:
        break
    zan -= H[i]

print(ans)