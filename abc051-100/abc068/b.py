# -*- coding: utf-8 -*-
def divide2(n):
    cnt = 0
    a = n
    while a != 1:
        if a % 2 == 1:
            return cnt
        else:
            a //= 2
            cnt += 1
    
    return cnt

N = int(input())
ans = 1
maxcnt = 0
for i in range(1,N+1):
    cnt = divide2(i)
    if cnt > maxcnt:
        ans = i
        maxcnt = cnt

print(ans)