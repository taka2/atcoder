# -*- coding: utf-8 -*-
n = int(input())
s = input()

isInQuote = False
result = ""
for i in range(n):
    if s[i] == '"' and isInQuote:
        isInQuote = False
        result = result + s[i]
    elif s[i] == '"' and (not isInQuote):
        isInQuote = True
        result = result + s[i]
    elif s[i] == ',' and (not isInQuote):
        result = result + "."
    else:
        result = result + s[i]

print(result)