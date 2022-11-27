# -*- coding: utf-8 -*-
import math
A,B= map(int, input().split())

def f(n):
    return (A/math.sqrt(n+1) + B*n)

l = 0
r = A//B

while((r - l) > 2):
    m1 = (l * 2 + r) // 3
    m2 = (l + r * 2) // 3
    if(f(m1) > f(m2)):
        l = m1
    else:
        r = m2

ans = A
for i in range(l, r+1):
    ans = min(ans, f(i))

print(ans)