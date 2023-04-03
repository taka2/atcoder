# -*- coding: utf-8 -*-
N = int(input())
fib = [0] * (10**7+1)
fib[1] = 1
fib[2] = 1

if N < 3:
    print(fib[N])
    exit(0)

modN = 10**9+7
for i in range(3,N+1):
    fib[i] = (fib[i-1] + fib[i-2]) % modN

print(fib[N])