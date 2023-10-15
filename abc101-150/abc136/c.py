# -*- coding: utf-8 -*-
N = int(input())
H = list(map(int, input().split()))

ans = True
for i in range(N-1, 0, -1):
    if H[i-1] - H[i] >= 2:
        ans = False
        break
    elif H[i-1] - H[i] == 1:
        H[i-1] -= 1

if ans:
    print("Yes")
else:
    print("No")