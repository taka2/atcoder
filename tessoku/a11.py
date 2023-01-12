# -*- coding: utf-8 -*-
N,X = map(int, input().split())
A = list(map(int, input().split()))
A.insert(0,0)

def search(x):
    l = 1
    r = N

    while(l<=r):
        m = (l+r)//2
        if x < A[m]:
            r = m - 1
        if x == A[m]:
            return m
        if x > A[m]:
            l = m + 1

ans = search(X)
print(ans)