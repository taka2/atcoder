# -*- coding: utf-8 -*-
import itertools

c = []
for i in range(3):
    c.append(list(map(int, input().split())))

clist = list(range(1,10))

def getNumberFromIndex(index):
    if index == 1:
        return (0,0,c[0][0])
    elif index == 2:
        return (0,1,c[0][1])
    elif index == 3:
        return (0,2,c[0][2])
    elif index == 4:
        return (1,0,c[1][0])
    elif index == 5:
        return (1,1,c[1][1])
    elif index == 6:
        return (1,2,c[1][2])
    elif index == 7:
        return (2,0,c[2][0])
    elif index == 8:
        return (2,1,c[2][1])
    else:
        return (2,2,c[2][2])

def isCross1(x,y):
    if x == 0 and y == 0:
        return True
    if x == 1 and y == 1:
        return True
    if x == 2 and y == 2:
        return True
    return False

def isCross2(x,y):
    if x == 2 and y == 0:
        return True
    if x == 1 and y == 1:
        return True
    if x == 0 and y == 2:
        return True
    return False

def isSameLine(xa,ya,xb,yb):
    if xa == xb or ya == yb:
        return True
    if xa == 0 and ya == 0 and xb == 1 and yb == 1:
        return True
    if xa == 0 and ya == 0 and xb == 2 and yb == 2:
        return True
    if xa == 1 and ya == 1 and xb == 0 and yb == 0:
        return True
    if xa == 1 and ya == 1 and xb == 2 and yb == 2:
        return True
    if xa == 2 and ya == 2 and xb == 0 and yb == 0:
        return True
    if xa == 2 and ya == 2 and xb == 1 and yb == 1:
        return True
    if xa == 2 and ya == 0 and xb == 1 and yb == 1:
        return True
    if xa == 2 and ya == 0 and xb == 0 and yb == 2:
        return True
    if xa == 1 and ya == 1 and xb == 2 and yb == 0:
        return True
    if xa == 1 and ya == 1 and xb == 0 and yb == 2:
        return True
    if xa == 0 and ya == 2 and xb == 2 and yb == 0:
        return True
    if xa == 0 and ya == 2 and xb == 1 and yb == 1:
        return True
    return False

gakkari = 0
sum = 0
for elem in itertools.permutations(clist,9):
    sum += 1
    index1 = elem[0]
    index2 = elem[1]
    index3 = elem[2]
    index4 = elem[3]
    index5 = elem[4]
    index6 = elem[5]
    index7 = elem[6]
    index8 = elem[7]
    index9 = elem[8]
    x1,y1,number1 = getNumberFromIndex(index1)
    x2,y2,number2 = getNumberFromIndex(index2)
    x3,y3,number3 = getNumberFromIndex(index3)
    x4,y4,number4 = getNumberFromIndex(index4)
    x5,y5,number5 = getNumberFromIndex(index5)
    x6,y6,number6 = getNumberFromIndex(index6)
    x7,y7,number7 = getNumberFromIndex(index7)
    x8,y8,number8 = getNumberFromIndex(index8)
    x9,y9,number9 = getNumberFromIndex(index9)

    row = [None,None,None]
    col = [None,None,None]
    cross1 = None
    cross2 = None

    col[x1] = number1
    row[y1] = number1
    if isCross1(x1,y1):
        cross1 = number1
    if isCross2(x1,y1):
        cross2 = number1

#2
    if col[x2] != None:
        if col[x2] == number2:
            gakkari += 1
            continue
        else:
            col[x2] = None
    else:
        col[x2] = number2
    if row[y2] != None:
        if row[y2] == number2:
            gakkari += 1
            continue
        else:
            row[y2] = None
    else:
        row[y2] = number2
    if isCross1(x2,y2):
        if cross1 != None:
            if cross1 == number2:
                gakkari += 1
                continue
            else:
                cross1 = None
        else:
            cross1 = number2
    if isCross2(x2,y2):
        if cross2 != None:
            if cross2 == number2:
                gakkari += 1
                continue
            else:
                cross2 = None
        else:
            cross2 = number2
#3
    if col[x3] != None:
        if col[x3] == number3:
            gakkari += 1
            continue
        else:
            col[x3] = None
    else:
        col[x3] = number3
    if row[y3] != None:
        if row[y3] == number3:
            gakkari += 1
            continue
        else:
            row[y3] = None
    else:
        row[y3] = number3
    if isCross1(x3,y3):
        if cross1 != None:
            if cross1 == number3:
                gakkari += 1
                continue
            else:
                cross1 = None
        else:
            cross1 = number3
    if isCross2(x3,y3):
        if cross2 != None:
            if cross2 == number3:
                gakkari += 1
                continue
            else:
                cross2 = None
        else:
            cross2 = number3
#4
    if col[x4] != None:
        if col[x4] == number4:
            gakkari += 1
            continue
        else:
            col[x4] = None
    else:
        col[x4] = number4
    if row[y4] != None:
        if row[y4] == number4:
            gakkari += 1
            continue
        else:
            row[y4] = None
    else:
        row[y4] = number4
    if isCross1(x4,y4):
        if cross1 != None:
            if cross1 == number4:
                gakkari += 1
                continue
            else:
                cross1 = None
        else:
            cross1 = number4
    if isCross2(x4,y4):
        if cross2 != None:
            if cross2 == number4:
                gakkari += 1
                continue
            else:
                cross2 = None
        else:
            cross2 = number4
#5
    if col[x5] != None:
        if col[x5] == number5:
            gakkari += 1
            continue
        else:
            col[x5] = None
    else:
        col[x5] = number5
    if row[y5] != None:
        if row[y5] == number5:
            gakkari += 1
            continue
        else:
            row[y5] = None
    else:
        row[y5] = number5
    if isCross1(x5,y5):
        if cross1 != None:
            if cross1 == number5:
                gakkari += 1
                continue
            else:
                cross1 = None
        else:
            cross1 = number5
    if isCross2(x5,y5):
        if cross2 != None:
            if cross2 == number5:
                gakkari += 1
                continue
            else:
                cross2 = None
        else:
            cross2 = number5
#6
    if col[x6] != None:
        if col[x6] == number6:
            gakkari += 1
            continue
        else:
            col[x6] = None
    else:
        col[x6] = number6
    if row[y6] != None:
        if row[y6] == number6:
            gakkari += 1
            continue
        else:
            row[y6] = None
    else:
        row[y6] = number6
    if isCross1(x6,y6):
        if cross1 != None:
            if cross1 == number6:
                gakkari += 1
                continue
            else:
                cross1 = None
        else:
            cross1 = number6
    if isCross2(x6,y6):
        if cross2 != None:
            if cross2 == number6:
                gakkari += 1
                continue
            else:
                cross2 = None
        else:
            cross2 = number6
#7
    if col[x7] != None:
        if col[x7] == number7:
            gakkari += 1
            continue
        else:
            col[x7] = None
    else:
        col[x7] = number7
    if row[y7] != None:
        if row[y7] == number7:
            gakkari += 1
            continue
        else:
            row[y7] = None
    else:
        row[y7] = number7
    if isCross1(x7,y7):
        if cross1 != None:
            if cross1 == number7:
                gakkari += 1
                continue
            else:
                cross1 = None
        else:
            cross1 = number7
    if isCross2(x7,y7):
        if cross2 != None:
            if cross2 == number7:
                gakkari += 1
                continue
            else:
                cross2 = None
        else:
            cross2 = number7
#8
    if col[x8] != None:
        if col[x8] == number2:
            gakkari += 1
            continue
        else:
            col[x8] = None
    else:
        col[x8] = number8
    if row[y8] != None:
        if row[y8] == number8:
            gakkari += 1
            continue
        else:
            row[y8] = None
    else:
        row[y8] = number8
    if isCross1(x8,y8):
        if cross1 != None:
            if cross1 == number8:
                gakkari += 1
                continue
            else:
                cross1 = None
        else:
            cross1 = number8
    if isCross2(x8,y8):
        if cross2 != None:
            if cross2 == number8:
                gakkari += 1
                continue
            else:
                cross2 = None
        else:
            cross2 = number8
#9
    if col[x9] != None:
        if col[x9] == number9:
            gakkari += 1
            continue
        else:
            col[x9] = None
    else:
        col[x9] = number9
    if row[y9] != None:
        if row[y9] == number9:
            gakkari += 1
            continue
        else:
            row[y9] = None
    else:
        row[y9] = number9
    if isCross1(x9,y9):
        if cross1 != None:
            if cross1 == number9:
                gakkari += 1
                continue
            else:
                cross1 = None
        else:
            cross1 = number9
    if isCross2(x9,y9):
        if cross2 != None:
            if cross2 == number9:
                gakkari += 1
                continue
            else:
                cross2 = None
        else:
            cross2 = number9

print(sum, gakkari)
print((sum-gakkari)/sum)