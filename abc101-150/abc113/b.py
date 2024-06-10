# -*- coding: utf-8 -*-
N = int(input())
T,A = map(int, input().split())
H = list(map(int, input().split()))

ans = -1
ansdiff = 99999999

for i in range(N):
    avgt = T-H[i]*0.006
    avgtdiff = abs(avgt-A)
    if avgtdiff < ansdiff:
        ans = i+1
        ansdiff = avgtdiff

print(ans)