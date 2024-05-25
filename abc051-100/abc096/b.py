# -*- coding: utf-8 -*-
A,B,C = map(int, input().split())
K = int(input())

ans = 0
maxABC = max(max(A,B), C)
if A == maxABC:
    ans = A * (2 ** K) + B + C
elif B == maxABC:
    ans = B * (2 ** K) + A + C
elif C == maxABC:
    ans = C * (2 ** K) + A + B

print(ans)