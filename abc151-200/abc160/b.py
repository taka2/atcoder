# -*- coding: utf-8 -*-
X = int(input())

yen500 = X // 500
yen5 = (X % 500) // 5

print(yen500 * 1000 + yen5 * 5)