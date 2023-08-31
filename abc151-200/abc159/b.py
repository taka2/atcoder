# -*- coding: utf-8 -*-
def isPalindrome(str):
    ret = True
    lenstr = len(str)
    for i in range(lenstr//2):
        if str[i] != str[lenstr-i-1]:
            ret = False
            break
    
    return ret

S = input()
leftS = S[:(len(S)-1)//2]
rightS = S[(len(S)+3)//2-1:]
if isPalindrome(S) and isPalindrome(leftS) and isPalindrome(rightS):
    print("Yes")
else:
    print("No")