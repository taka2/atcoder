# -*- coding: utf-8 -*-
n,k,q = map(int, input().split())
a = list(map(int, input().split()))
l = list(map(int, input().split()))

pos = {}
for i in range(k):
    pos[i+1] = a[i]

for i in range(q):
    targetPos = pos[l[i]]
    #print(pos, i, targetPos,l[i], k)

    # 端のポジションにいる場合
    if targetPos == n:
        pass
    
    # 右となりのコマが存在する場合
    elif l[i] < k and pos[l[i]+1] == targetPos+1:
        pass

    # 上記以外
    else:
        pos[l[i]] = targetPos + 1

result = []
for i in pos:
    result.append(str(pos[i]))

print(" ".join(result))
