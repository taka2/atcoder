# -*- coding: utf-8 -*-
X,N = map(int, input().split())
p = list(map(int, input().split()))

ans = 99999
diff = 99999

for i in range(102):
    if i in p:
        continue
    d = abs(i - X)
    if d < diff:
        ans = i
        diff = d

print(ans)