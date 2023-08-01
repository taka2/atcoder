# -*- coding: utf-8 -*-
N = int(input())

ans = 0
for i in range(1,N+1):
    strdec = str(i)
    stroct = oct(i)[2:]
    if "7" in strdec or "7" in stroct:
        pass
    else:
        ans += 1

print(ans)