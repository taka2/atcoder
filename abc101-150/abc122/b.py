# -*- coding: utf-8 -*-
S = input()

ansList = []
current = 0
for i in range(len(S)):
    if S[i] in 'ACGT':
        current += 1
    else:
        ansList.append(current)
        current = 0
ansList.append(current)

ans = max(ansList)
print(ans)