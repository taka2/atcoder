# -*- coding: utf-8 -*-
N = int(input())

yakusuu = []
for i in range(1,10):
    if N % i == 0:
        yakusuu.append(i)

ans = ""
for i in range(N+1):
    ketaans = -1
    for j in range(len(yakusuu)):
        if i % (N // yakusuu[j]) == 0:
            ketaans = yakusuu[j]
            break
    if ketaans == -1:
        ans += "-"
    else:
        ans += str(ketaans)

print(ans)