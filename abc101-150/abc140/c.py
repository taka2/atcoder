# -*- coding: utf-8 -*-
N = int(input())
B = list(map(int, input().split()))

ans = B[0]
for i in range(N-1):
    if i != N-2 and B[i] > B[i+1]:
        ans += B[i+1]
    else:
        ans += B[i]

print(ans)