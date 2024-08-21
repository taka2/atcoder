# -*- coding: utf-8 -*-
N,M = map(int, input().split())
S = input()
T = input()

f = T.startswith(S)
e = T.endswith(S)

if f and e:
    print(0)
elif f and not e:
    print(1)
elif not f and e:
    print(2)
else:
    print(3)