# -*- coding: utf-8 -*-
N = int(input())
D = []
for i in range(N):
    D1,D2 = map(int, input().split())
    D.append((D1,D2))

count = 0
ans = False
for i in range(N):
    (D1,D2) = D[i]
    if D1==D2:
        count += 1
        if count == 3:
            ans = True
            break
    else:
        count = 0

if ans:
    print("Yes")
else:
    print("No")