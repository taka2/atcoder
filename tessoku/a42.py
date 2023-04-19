# -*- coding: utf-8 -*-
N,K = map(int, input().split())
AB = []
for i in range(N):
    A,B = map(int, input().split())
    AB.append((A,B))

def judge(a,b):
    ret = 0
    for i in range(N):
        (A,B) = AB[i]
        if A >= a and A <= (a+K) and B >= b and B <= (b+K):
            ret += 1
    return ret

ans = 0
for a in range(1,101):
    for b in range(1,101):
        ans = max(ans, judge(a,b))

print(ans)