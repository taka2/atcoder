# -*- coding: utf-8 -*-
# スペース区切りの整数の入力
x,y,n = map(int, input().split())

if(x*3 > y):
    yn = n//3
    print(y*yn + x*(n-yn*3))
else:
    print(x*n)