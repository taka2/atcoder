# -*- coding: utf-8 -*-
N,K = map(int, input().split())

def g1(x):
    return int("".join(sorted(str(x), reverse=True)))

def g2(x):
    return int("".join(sorted(str(x))))

def f(x):
    return g1(x) - g2(x)

prev = N
for i in range(1,K+1):
    prev = f(prev)

print(prev)