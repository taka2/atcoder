# -*- coding: utf-8 -*-
X = int(input())

ans = -1
if X < 40:
    ans = 40-X
elif X < 70:
    ans = 70-X
elif X < 90:
    ans = 90-X
else:
    print("expert")
    exit(0)
print(ans)