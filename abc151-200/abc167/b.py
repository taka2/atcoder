# -*- coding: utf-8 -*-
A,B,C,K = map(int, input().split())

ans = 0
zan = K
Amai = min(A,zan)
ans += Amai
zan -= Amai

Bmai = min(B,zan)
zan -= Bmai

Cmai = min(C,zan)
ans -= Cmai

print(ans)