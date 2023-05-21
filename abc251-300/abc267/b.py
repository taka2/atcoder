# -*- coding: utf-8 -*-
S = list("0" + input())

lanes = []
lanes.append([])
lanes.append([7])
lanes.append([4])
lanes.append([2,8])
lanes.append([1,5])
lanes.append([3,9])
lanes.append([6])
lanes.append([10])

# 指定したレーンのピンがどれか1つでも立ってたらTrueを返す
def isStand(lane):
    targetLane = lanes[lane]
    for i in range(len(targetLane)):
        if S[targetLane[i]] == '1':
            return True
    return False

# 指定したレーンのピンがすべて倒れていたらTrueを返す
def isNotStand(lane):
    targetLane = lanes[lane]
    for i in range(len(targetLane)):
        if S[targetLane[i]] == '1':
            return False
    return True

# スプリット判定する
def check(lanea, laneb):
    #print("check", lanea, laneb)
    if(isStand(lanea) and isStand(laneb)):
        #print("isStand=true")
        for i in range(laneb-lanea-1):
            targetLaneNumber = i+lanea+1
            if isNotStand(targetLaneNumber):
                #print("isNotStand=true", targetLaneNumber)
                return True
    return False

def checkAndPrint(lanea, laneb):
    if(check(lanea, laneb)):
        print("Yes")
        exit(0)

if(S[1] == '0'):
    checkAndPrint(1,7)
    checkAndPrint(1,6)
    checkAndPrint(1,5)
    checkAndPrint(1,4)
    checkAndPrint(1,3)
    checkAndPrint(2,7)
    checkAndPrint(2,6)
    checkAndPrint(2,5)
    checkAndPrint(2,4)
    checkAndPrint(3,7)
    checkAndPrint(3,6)
    checkAndPrint(3,5)
    checkAndPrint(4,7)
    checkAndPrint(4,6)
    checkAndPrint(5,7)
    print("No")
else:
    print("No")