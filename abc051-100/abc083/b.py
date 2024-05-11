# -*- coding: utf-8 -*-
N,A,B = map(int, input().split())

def sumketa(n):
    ret = 0
    while n > 0:
        ret += n % 10
        n //= 10
    return ret

ans = 0
for i in range(1,N+1):
    sumketai = sumketa(i)
    if sumketai >= A and sumketai <= B:
        ans += i

print(ans)