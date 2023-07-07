# -*- coding: utf-8 -*-
import itertools

S,K = input().split()
K = int(K)
sortedS = sorted(list(S))
SS = ""
for i in range(len(S)):
    SS += sortedS[i]

dup = {}
count = 0

for elem in itertools.permutations(SS, len(SS)):
    if str(elem) in dup:
        continue
    else:
        dup[str(elem)] = 1

    count += 1
    if count == K:
        ans = ""
        for i in range(len(elem)):
            ans += elem[i]
        print(ans)
        exit(0)