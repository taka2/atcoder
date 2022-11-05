# -*- coding: utf-8 -*-
from decimal import Decimal, getcontext, ROUND_HALF_UP
 
# スペース区切りの整数の入力
x, k = map(int, input().split())
 
a = Decimal(x)
for num in range(k):
    a = a/10**(num+1)
    a = a.quantize(Decimal("0"), rounding=ROUND_HALF_UP)
    a = a*10**(num+1)
 
print(a)