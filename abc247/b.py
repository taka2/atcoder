# -*- coding: utf-8 -*-
N = int(input())
list = []
for i in range(N):
    s,t = map(str, input().split())
    list.append((s,t))

ans = True
for i in range(N):
    (s,t) = list[i]
    sflag = True
    tflag = True
    for j in range(i,N):
        if i == j:
            continue
        (s1,t1) = list[j]
        if s == s1 or s == t1:
            sflag = False
        if t == s1 or t == t1:
            tflag = False
        if not sflag and not tflag:
            break
    
    if not sflag and not tflag:
        ans = False
        break

if ans:
    print("Yes")
else:
    print("No")