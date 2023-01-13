# -*- coding: utf-8 -*-
N = float(input())

def calc(x):
    return (x**3 + x)

l = 0.0001
r = 50.0
while(l<=r):
    m = (l+r)/2
    calculated = calc(m)
    if abs(N - calculated) <= 0.0001:
        break
    if calculated > N:
        r = m - 0.0001
    if calculated < N:
        l = m + 0.0001

print(m)