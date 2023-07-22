# -*- coding: utf-8 -*-
N,D = map(int, input().split())
S = []
for i in range(N):
    S.append(input())

ans = 0
renzoku = 0
for i in range(D):
    flag = True
    for j in range(N):
        if S[j][i] == 'x':
            flag = False
            break
    
    if flag:
        renzoku += 1
    else:
        ans = max(ans, renzoku)
        renzoku = 0

ans = max(ans, renzoku)
print(ans)
