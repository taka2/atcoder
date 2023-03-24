# -*- coding: utf-8 -*-
S = input()
T = ""
for i in range(0, len(S), 2):
  T += S[i+1]
  T += S[i]
  
print(T)