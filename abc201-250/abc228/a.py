# -*- coding: utf-8 -*-
S,T,X = map(int, input().split())
 
if T>S and X>=S and X<T:
  print("Yes")
elif S>T and (X>=S or X<T):
  print("Yes")
else:
  print("No")