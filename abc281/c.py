# -*- coding: utf-8 -*-
n,t = map(int, input().split())
a = list(map(int, input().split()))

# 累積和
sum = 0
suma = []
for i in range(n):
    sum += a[i]
    suma.append(sum)

pos = t % sum
for i in range(n):
    if pos < suma[i]:
        prevpos = 0
        if i != 0:
            prevpos = suma[i-1]
        
        print(i+1, pos-prevpos)
        break