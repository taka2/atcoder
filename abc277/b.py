# -*- coding: utf-8 -*-
firstChars = ['H', 'D', 'C', 'S']
secondChars = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
map = {}

def check(s):
    if s[0] in firstChars and s[1] in secondChars and (not s in map):
        map[s] = 1
        return True
    else:
        return False

# 整数の入力
n = int(input())
list = []
for i in range(n):
    list.append(input())

result = "Yes"
for i in range(n):
    s = list[i]
    if not check(s):
        result = "No"
        break

print(result)