# -*- coding: utf-8 -*-
import bisect

N,M,D = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
sortedB = sorted(B)

ans = -1
for i in range(N):
    Ai = A[i]
    Bmin = Ai-D
    Bmax = Ai+D
    left = 0
    right = len(B)-1
    while(left <= right):
        mid = (left+right)//2
        if sortedB[mid] < Bmin:
            left = mid+1
        elif sortedB[mid] > Bmax:
            right = mid-1
        elif sortedB[mid] < Ai:
            ans = max(ans, Ai+sortedB[mid])
            left = mid+1
        elif sortedB[mid] > Ai:
            ans = max(ans, Ai+sortedB[mid])
            right = mid-1
        else:
            ans = max(ans, Ai+sortedB[mid])
            left = mid+1
            right = mid

print(ans)