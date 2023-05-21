# -*- coding: utf-8 -*-
def paddingBinary(binaryList, n):
    resultList = binaryList
    for i in range(n - len(binaryList)):
        resultList.insert(0, '0')
    return resultList
    
def fromBinaryListToN(binaryList):
    listLen = len(binaryList)
    sum = 0
    for i in range(listLen):
        if(binaryList[i] == '1'):
            sum += 2 ** (listLen - i - 1)

    return sum

n = int(input())

if n == 0:
    print("0")
    exit(0)

binaryList = list(bin(n)[2:])
countOne = 0
onePositions = []
for i in range(len(binaryList)):
    if binaryList[i] == '1':
        countOne += 1
        onePositions.append(i)

for i in range(2**countOne):
    replaceBinaryList = paddingBinary(list(bin(i)[2:]), countOne)
    copyBinaryList = binaryList.copy()
    for j in range(len(replaceBinaryList)):
        copyBinaryList[onePositions[j]] = replaceBinaryList[j]
    print(fromBinaryListToN(copyBinaryList))
