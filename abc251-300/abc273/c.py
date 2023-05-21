# -*- coding: utf-8 -*-
# 整数の入力
n = int(input())
# スペース区切りの整数の入力
a = list(map(int, input().split()))
 
mp = {}
for i in range(len(a)):
    if a[i] in mp:
        mp[a[i]] = mp[a[i]] + 1
    else:
        mp[a[i]] = 1
 
reverseSortedKey = sorted(list(mp.keys()), reverse=True)
for i in range(len(reverseSortedKey)):
    print(mp[reverseSortedKey[i]])
 
for i in range(n-len(mp)):
    print("0")