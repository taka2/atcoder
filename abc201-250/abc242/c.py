# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10000000)

N = int(input())

ans = [0]
mod = 998244353

def search(i):
    if len(str(i)) == N:
        ans[0] += 1
        return
    
    if i+1 <= 9:
        search(i*10 + (i+1))
    search(i*10 + i)
    if i-1 >= 1:
        search(i*10 + (i-1))

for i in range(1, 10):
    search(i)

print(ans[0] % mod)