# -*- coding: utf-8 -*-
N = int(input())
S = input()

ans = S.find("ABC")
if ans == -1:
    print(-1)
else:
    print(ans+1)