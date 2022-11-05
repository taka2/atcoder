# -*- coding: utf-8 -*-
def recur(n):
    if n == 0:
        return 1
    else:
        return n * recur(n-1)
 
 
# 整数の入力
a = int(input())
print(recur(a))