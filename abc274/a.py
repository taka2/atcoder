# -*- coding: utf-8 -*-
from decimal import Decimal, getcontext, ROUND_HALF_UP

# スペース区切りの整数の入力
a, b = map(int, input().split())
a = Decimal(a)
b = Decimal(b)
c = b/a
c = c * 1000
c = c.quantize(Decimal("0"), rounding=ROUND_HALF_UP)
c = c/1000
print('{:.3f}'.format(c))
