# -*- coding: utf-8 -*-
import re

S = input()
pattern = r'^A*B*C*$'
if re.match(pattern, S) != None:
    print("Yes")
else:
    print("No")