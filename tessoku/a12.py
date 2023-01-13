# -*- coding: utf-8 -*-
N,K = map(int, input().split())
A = list(map(int, input().split()))

def sumPrinter(x):
    result = 0
    for i in range(N):
        result += x // A[i]
    return result

l = 1
r = 10**9

while(l<r):
    m = (l+r)//2
    printedCount = sumPrinter(m)
    if printedCount >= K:
        r = m
    else:
        l = m + 1

print(l)