# -*- coding: utf-8 -*-
S1 = input()
S2 = input()
 
if S1[0] == '.' and S2[1] == '.':
  print("No")
elif S1[1] == '.' and S2[0] == '.':
  print("No")
else:
  print("Yes")