# -*- coding: utf-8 -*-
a = int(input())
b = int(input())

diff = abs(a-b)
diff10 = 10-diff

print(min(diff, diff10))