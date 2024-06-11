# -*- coding: utf-8 -*-
S = list(map(int, input().split()))

prev = -1
ans = True
for i in range(8):
    if S[i] >= prev and S[i] >= 100 and S[i] <= 675 and S[i] % 25 == 0:
        prev = S[i]
    else:
        ans = False
        break

if ans:
    print("Yes")
else:
    print("No")