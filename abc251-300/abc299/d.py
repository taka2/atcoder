# -*- coding: utf-8 -*-
N = int(input())

l = 1
r = N

ans = -1
while(l<=r):
    m = (l+r)//2
    print("?",m)
    X = int(input())
    if m == l+1 and X == 1:
        ans = m-1
        break
    elif m == r-1 and X == 0:
        ans = m
        break
    elif X == 1:
        r = m
    elif X == 0:
        l = m

print("!",ans)