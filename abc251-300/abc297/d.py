# -*- coding: utf-8 -*-
A,B = map(int, input().split())

ans = 0
while A != B:
    if A>B:
        if A%B == 0:
            ans += (A-B)//B
            A = B
        else:
            ans += A // B
            A = A % B
    else:
        if B%A == 0:
            ans += (B-A)//A
            B = A
        else:
            ans += B // A
            B = B % A

print(ans)