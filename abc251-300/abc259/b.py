# -*- coding: utf-8 -*-
# see https://keisan.casio.jp/exec/system/1496883774
import math
A,B,D = map(int, input().split())

Adash = A * math.cos(math.radians(D)) - B * math.sin(math.radians(D))
Bdash = A * math.sin(math.radians(D)) + B * math.cos(math.radians(D))

print(Adash, Bdash)