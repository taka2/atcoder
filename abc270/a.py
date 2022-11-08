# -*- coding: utf-8 -*-
# スペース区切りの整数の入力
a,b = map(int, input().split())

a1 = a//4
a2 = (a-(a1*4)) // 2
a3 = (a - (a1*4) - (a2*2))
b1 = b//4
b2 = (b-(b1*4)) // 2
b3 = (b - (b1*4) - (b2*2))

score = 0
if(a1==1 or b1==1):
    score += 4
if(a2==1 or b2==1):
    score += 2
if(a3==1 or b3==1):
    score += 1

print(score)