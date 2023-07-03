# -*- coding: utf-8 -*-
a = list(map(int, input().split()))
sorteda = sorted(a)

if sorteda[1] - sorteda[0] == sorteda[2] - sorteda[1]:
    print("Yes")
else:
    print("No")