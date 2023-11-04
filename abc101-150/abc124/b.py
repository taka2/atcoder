# -*- coding: utf-8 -*-
N = int(input())
H = list(map(int, input().split()))

ans = 1
for i in range(1,N):
    flag = True
    for j in range(i):
        if H[j] <= H[i]:
            pass
        else:
            flag = False
            break
    
    if flag:
        ans += 1

print(ans)