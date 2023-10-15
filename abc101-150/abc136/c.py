# -*- coding: utf-8 -*-
N = int(input())
H = list(map(int, input().split()))

ans = True
prev = False
for i in range(N-1):
    if H[i] - H[i+1] >= 2:
        ans = False
        break
    elif H[i] - H[i+1] == 1:
        if prev:
            ans = False
            break
        else:
            prev = True
    else:
        prev = False

if ans:
    print("Yes")
else:
    print("No")