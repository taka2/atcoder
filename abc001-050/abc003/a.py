# -*- coding: utf-8 -*-
N = int(input())
sum = 0
for i in range(1,N+1):
    sum += i
avg = sum / N
ans = avg * 10000
print(ans)