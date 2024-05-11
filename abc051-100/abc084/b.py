# -*- coding: utf-8 -*-
import re

A,B = map(int, input().split())
S = input()

pattern = r'\d{'+str(A)+'}-\d{'+str(B)+'}'
if re.match(pattern, S) != None:
    print("Yes")
else:
    print("No")