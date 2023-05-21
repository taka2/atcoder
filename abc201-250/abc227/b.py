# -*- coding: utf-8 -*-
N = int(input())
S = list(map(int, input().split()))

ans = 0
for i in range(N):
    Si = S[i]
    flag = True
    for a in range(1, 200):
        for b in range(1, 200):
            SS = 4*a*b + 3*a + 3*b
            if Si == SS:
                flag = False
                break
    if flag:
        ans += 1

print(ans)