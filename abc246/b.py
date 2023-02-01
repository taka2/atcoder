# -*- coding: utf-8 -*-
import math
X,Y = map(int, input().split())

distance = math.sqrt(X**2 + Y**2)
x = X/distance
y = Y/distance
print(x,y)