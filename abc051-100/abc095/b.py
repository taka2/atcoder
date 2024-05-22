# -*- coding: utf-8 -*-
N,X = map(int, input().split())
m = []
for i in range(N):
    m.append(int(input()))

summ = 0
for i in range(N):
    summ += m[i]

minm = min(m)

zan = X - summ
ans = N

ans += (zan // minm)

print(ans)