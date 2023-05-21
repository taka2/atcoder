# -*- coding: utf-8 -*-
import re

s = input()
if re.match(r'[A-Z][1-9]\d\d\d\d\d[A-Z]', s):
    print("Yes")
else:
    print("No")