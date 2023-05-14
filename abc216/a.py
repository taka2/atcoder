# -*- coding: utf-8 -*-
X,Y = map(int, input().split("."))

if Y>=0 and Y<=2:
    print(str(X) +"-")
elif Y >=3 and Y <= 6:
    print(str(X))
else:
    print(str(X) + "+")
