# -*- coding: utf-8 -*-
A,B,X = map(int, input().split())

if (X-A) >= 0 and B >= (X-A):
    print("YES")
else:
    print("NO")