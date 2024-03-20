# -*- coding: utf-8 -*-
def countA(str):
    ret = 0
    for i in range(len(str)):
        if str[i] == "a":
            ret += 1
    return ret

A = input()
if A == "a":
    print(-1)
else:
    ans = ""
    for i in range(len(A)):
        ans += "a"
    if countA(A) == len(A):
        print(ans[:-1])
    else:
        print(ans)