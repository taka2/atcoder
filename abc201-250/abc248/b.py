# -*- coding: utf-8 -*-
A,B,K = map(int, input().split())

ans = 0
current = A
while(current < B):
    current *= K
    ans += 1

print(ans)