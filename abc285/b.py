# -*- coding: utf-8 -*-
N = int(input())
S = "0" + input()

for i in range(1,N):
    ans = 0
    for k in range(1,(N-i+1)):
        S1 = S[k]
        S2 = S[k+i]
        if S1 == S2:
            break
        else:
            ans += 1
    print(ans)
