# -*- coding: utf-8 -*-
N = int(input())
L = sorted(list(map(int, input().split())))

ans = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            a = L[i]
            b = L[j]
            c = L[k]
            if a != b and b != c and c < a+b:
                ans += 1

print(ans)