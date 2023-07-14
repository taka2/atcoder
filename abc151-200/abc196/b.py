# -*- coding: utf-8 -*-
X = input()
ans = ""
for i in range(len(X)):
    if X[i] == ".":
        break
    else:
        ans += X[i]

print(ans)