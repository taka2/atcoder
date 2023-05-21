# -*- coding: utf-8 -*-
S = input()

result = 0
while len(S) > 0:
    if S[-2:] == "00":
        S = S[0:-2]
    else:
        S = S[0:-1]
    result += 1

print(result)