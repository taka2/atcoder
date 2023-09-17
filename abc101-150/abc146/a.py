# -*- coding: utf-8 -*-
S = input()
week = ["SAT","FRI","THU","WED","TUE","MON","SUN"]

for i in range(len(week)):
    if week[i] == S:
        print(i+1)
        break