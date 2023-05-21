# -*- coding: utf-8 -*-
S = input()
a,b = map(int, input().split())

cha = S[a-1]
chb = S[b-1]

print(S[0:a-1] + chb + S[a:b-1] + cha + S[b:])