# -*- coding: utf-8 -*-
import math
from decimal import *

A,B = map(int, input().split())
print(Decimal(A)*Decimal(B)/Decimal(math.gcd(A,B)))