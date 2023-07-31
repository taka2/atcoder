# -*- coding: utf-8 -*-
N,X = map(int, input().split())
VP = []
for i in range(N):
    V,P = map(int, input().split())
    VP.append((V,P))

sumAlcohol = 0
ans = -1
for i in range(N):
    (V,P) = VP[i]
    sumAlcohol += V*P
    if sumAlcohol > X*100:
        ans = i+1
        break

print(ans)