# -*- coding: utf-8 -*-
K = int(input())

keta = []
while K>0:
    keta.append(K%2)
    K = K//2

ans = ""
for i in range(len(keta)-1, -1, -1):
    if keta[i] == 0:
        ans += "0"
    else:
        ans += "2"
print(ans)