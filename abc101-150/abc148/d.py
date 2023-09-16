# -*- coding: utf-8 -*-
N = int(input())
a = list(map(int, input().split()))

ans = 0
currentNumber = 1

for i in range(N):
    if a[i] == currentNumber:
        currentNumber += 1
    else:
        ans += 1

if currentNumber == 1:
    print(-1)
else:
    print(ans)