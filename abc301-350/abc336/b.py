# -*- coding: utf-8 -*-
N = int(input())
binstr = bin(N)

ans = 0
for i in range(len(binstr)-1,-1,-1):
    if binstr[i] == '0':
        ans += 1
    else:
        break

print(ans)