# -*- coding: utf-8 -*-
S = input()

n = len(S)
x = 0
for i in range(n):
    if S[i] == 'a':
        x += 1
    else:
        break

y = 0
for i in range(n-1, -1, -1):
    if S[i] == 'a':
        y += 1
    else:
        break

# すべてがa
if x == n:
    print("Yes")
    exit(0)

# 前のaが多い
if x > y:
    print("No")
    exit(0)

# 間が回文かどうか調べる
for i in range(x, n-y):
    if S[i] != S[x+n-y-i-1]:
        print("No")
        exit(0)

print("Yes")