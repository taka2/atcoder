# -*- coding: utf-8 -*-
# 整数の入力
n = int(input())

hexStr = hex(n)


print(hexStr.lstrip("0x").upper().zfill(2))