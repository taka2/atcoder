# -*- coding: utf-8 -*-
A,B,C,D = map(int, input().split())

ans = -1
diff = C*D-B
if diff > 0:
    ans = (A+diff-1)//diff
print(ans)