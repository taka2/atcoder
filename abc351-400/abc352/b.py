# -*- coding: utf-8 -*-
S = input()
T = input()

current = 0
ans = []
for i in range(len(T)):
    if T[i] == S[current]:
        ans.append(i+1)
        current += 1

print(*ans)