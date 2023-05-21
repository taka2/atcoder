# -*- coding: utf-8 -*-
import math

# 整数の入力
n = int(input())
a = list(map(int, input().split()))

g = 0
for i in range(n):
    g = math.gcd(g, a[i])

result = 0
for i in range(n):
    a[i] /= g
    while(a[i] % 2 == 0):
        a[i] = a[i] // 2
        result += 1
    
    while(a[i] % 3 == 0):
        a[i] = a[i] // 3
        result += 1
    
    if(a[i] != 1):
        print(-1)
        exit(0)

print(result)