# -*- coding: utf-8 -*-
X = int(input())

ans = 0
for i in range(1,32):
    for j in range(2,10):
        if i**j <= X:
            ans = max(ans, i**j)

print(ans)