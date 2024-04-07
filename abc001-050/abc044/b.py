# -*- coding: utf-8 -*-
from collections import defaultdict
w = input()
wcount = defaultdict(int)

for i in range(len(w)):
    wcount[w[i]] += 1

ans = True
for key in wcount:
    if wcount[key] % 2 != 0:
        ans = False
        break

if ans:
    print("Yes")
else:
    print("No")