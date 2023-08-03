# -*- coding: utf-8 -*-
N,M,T = map(int, input().split())
AB = []
for i in range(M):
    A,B = map(int, input().split())
    AB.append((A,B))

current = N
currentTime = 0
ans = True
for i in range(M):
    (A,B) = AB[i]
    print(A,B,current,currentTime)
    if current < A-currentTime:
        ans = False
        break
    else:
        current = min(N,current-A+(B-A))
        currentTime = B

if current < (T-currentTime):
    ans = False

if ans:
    print("Yes")
else:
    print("No")