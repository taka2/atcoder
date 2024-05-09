# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))

ans = 0
while True:
    flag = True
    for i in range(N):
        if A[i] % 2 == 0:
            A[i] //= 2
        else:
            flag = False
            break
    
    if flag:
        ans += 1
    else:
        break

print(ans)