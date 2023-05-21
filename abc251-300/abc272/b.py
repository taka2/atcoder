# -*- coding: utf-8 -*-
import itertools

# 整数の入力
n,m = map(int, input().split())

events = []
for i in range(m):
    persons = list(map(int, input().split()))
    persons.pop(0)
    events.append(persons)

result = True
for combi in itertools.combinations(list(range(n)), 2):
    eventResult = False
    person1 = combi[0]+1
    person2 = combi[1]+1
    #print("combi=", combi, person1, person2)
    # すべてのイベントを順番にチェックしてどこかに入っていればOK
    for event in events:
        #print("event=",event)
        if person1 in event and person2 in event:
            eventResult = True
            break

    # どのイベントにも入っていなければNG
    if(not eventResult):
        result = False
        break

if(result):
    print("Yes")
else:
    print("No")