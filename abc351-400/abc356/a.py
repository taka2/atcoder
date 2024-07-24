# -*- coding: utf-8 -*-
N,L,R = map(int, input().split())

ans = []
for i in range(1,L):
    ans.append(i)

for i in range(R,L-1,-1):
    ans.append(i)

for i in range(R+1,N+1):
    ans.append(i)

print(*ans)