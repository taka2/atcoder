# -*- coding: utf-8 -*-
from collections import defaultdict
 
S = input()
mapS = defaultdict(int)
 
for i in range(len(S)):
  mapS[S[i]] += 1
  
if len(mapS) == 1:
  print("1")
elif len(mapS) == 2:
  print("3")
else:
  print("6")