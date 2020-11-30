import numpy as np
from scipy.spatial import distance
import sys


def normalize(input, array):
    f = open(input, "r")
    s = f.read().replace('W', '1')
    s = s.replace('R', '0')
    f.close();
    rowsNum = 0
    for line in s.splitlines():
        rowsNum += 1
        array.append(line.split(","))
    rowLen = len(array[0])

    for i in range(rowsNum):
        for j in range(rowLen):
            if (array[i][j] == "1\n"):
                array[i][j] = "1"
            if (array[i][j] == "0\n"):
                array[i][j] = "0"
            array[i][j] = float(array[i][j])
    XminCol = []
    XminCol.append(array[0].copy())
    for i in range(rowsNum):
        for j in range(rowLen):
            if array[i][j] < XminCol[0][j]:
                XminCol[0][j] = array[i][j]

    XmaxCol = []
    XmaxCol.append(array[0].copy())
    for i in range(rowsNum):
        for j in range(rowLen):
            if array[i][j] > XmaxCol[0][j]:
                XmaxCol[0][j] = array[i][j]

    for i in range(rowsNum):
        for j in range(rowLen):
            array[i][j] = (array[i][j] - XminCol[0][j]) / (XmaxCol[0][j] - XminCol[0][j])


def main():
    trainExemple = sys.argv[1]
    trainLabels = sys.argv[2]
    testExemple = sys.argv[3]
    array_trainx = []
    array_testx = []
    array_trainy = []
    f = open(trainLabels, "r")
    for line in f:
        array_trainy.append(int(line))
    f.close()
    normalize(trainExemple, array_trainx)
    normalize(testExemple, array_testx)
    largestInex = []
    resultsKNN = []
    k = 7
    cntr=0
    for i in array_testx:
        dist_table = []
        for j in array_trainx:
            dist_table.append(distance.euclidean(i, j))
        largestInex.append(sorted(range(len(dist_table)), key=lambda sub: dist_table[sub])[-k:])
        zeroCntr = 0
        oneCntr = 0
        twoCntr = 0
        for index in largestInex[cntr]:
            if array_trainy[index] == 0:
                zeroCntr += 1
            elif array_trainy[index] == 1:
                oneCntr += 1
            elif array_trainy[index] == 2:
                twoCntr += 1
        if zeroCntr==max(zeroCntr, oneCntr, twoCntr):
            resultsKNN.append(0)
        elif oneCntr==max(zeroCntr, oneCntr, twoCntr):
            resultsKNN.append(1)
        else:
            resultsKNN.append(2)
        cntr+=1
    print("sfc")


if __name__ == '__main__':
    main()
