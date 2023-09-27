# -*- coding: utf-8 -*-
import math

A,B = map(int, input().split())

ans = 1 + math.ceil((B-A) / (A-1))
print(ans)