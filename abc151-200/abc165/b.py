# -*- coding: utf-8 -*-
X = int(input())

ans = 0
money = 100
while money < X:
    money = money + money // 100
    ans += 1

print(ans)