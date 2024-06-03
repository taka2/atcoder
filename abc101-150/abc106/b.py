# -*- coding: utf-8 -*-
N = int(input())

def numYakusuu(n):
    ret = 0
    for i in range(1,n+1):
        if n % i == 0:
            ret += 1
    return ret

ans = 0
for i in range(1,N+1,2):
    num = numYakusuu(i)
    if num == 8:
        ans += 1

print(ans)