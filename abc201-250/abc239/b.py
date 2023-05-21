# -*- coding: utf-8 -*-
from decimal import *

X = Decimal(int(input()))
Y = X/Decimal(10)
print(Y.quantize(Decimal(1), ROUND_FLOOR))