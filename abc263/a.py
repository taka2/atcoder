# -*- coding: utf-8 -*-
# スペース区切りの整数の入力
num = list(map(int, input().split()))

map = {}
for i in range(len(num)):
    if num[i] in map:
        map[num[i]] += 1
    else:
        map[num[i]] = 1

values = sorted(map.values())
if len(map) == 2 and values[0] == 2 and values[1] == 3:
    print("Yes")
else:
    print("No")