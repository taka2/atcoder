# -*- coding: utf-8 -*-
from collections import defaultdict
s = input()

map = defaultdict(int)
for i in range(len(s)):
    c = s[i:i+1]
    map[c] += 1

for ch in map:
    if map[ch] == 1:
        print(ch)
        break
else:
    print("-1")