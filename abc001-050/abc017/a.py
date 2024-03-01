# -*- coding: utf-8 -*-
s1,e1 = map(int, input().split())
s2,e2 = map(int, input().split())
s3,e3 = map(int, input().split())

ans = 0
ans += int(s1*e1/10)
ans += int(s2*e2/10)
ans += int(s3*e3/10)

print(ans)