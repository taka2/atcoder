# -*- coding: utf-8 -*-
N = int(input())

keta1 = N % 10
if keta1 == 2 or keta1 == 4 or keta1 == 5 or keta1 == 7 or keta1 == 9:
    print("hon")
elif keta1 == 3:
    print("bon")
else:
    print("pon")