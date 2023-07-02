# -*- coding: utf-8 -*-
S = input()

mapA = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}

ans = ""
for i in range(len(S)-1, -1, -1):
    ans += mapA[S[i]]

print(ans)