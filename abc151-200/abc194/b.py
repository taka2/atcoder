# -*- coding: utf-8 -*-
N = int(input())
AB = []
for i in range(N):
    A,B = map(int, input().split())
    AB.append((A,B))

ans = 10**12
for i in range(N):
    for j in range(N):
        ABi = AB[i]
        ABj = AB[j]
        if i==j:
            time = ABi[0] + ABj[1]
        else:
            time = max(ABi[0], ABj[1])
        ans = min(ans, time)
    
print(ans)