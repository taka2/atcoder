# -*- coding: utf-8 -*-
N,K = map(int, input().split())

ans = 0
for i in range(1,N+1):
    for j in range(1,K+1):
        strNumber = str(i)+"0"+str(j)
        number = int(strNumber)
        ans += number
    
print(ans)