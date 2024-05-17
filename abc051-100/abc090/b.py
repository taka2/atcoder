# -*- coding: utf-8 -*-
def isPalindrome(str):
    ret = True
    lenstr = len(str)
    for i in range(lenstr//2):
        if str[i] != str[lenstr-i-1]:
            ret = False
            break
    
    return ret

A,B = map(int, input().split())

ans = 0
for i in range(A,B+1):
    if isPalindrome(str(i)):
        ans += 1

print(ans)