import numpy as np
from scipy.spatial import distance
import sys
import copy

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
    #noramilze train_x
    f = open(trainExemple, "r")
    s = f.read().replace('W', '1')
    s = s.replace('R', '0')
    f.close();
    rowsNum = 0
    for line in s.splitlines():
        rowsNum += 1
        array_trainx.append(line.split(","))
    rowLen = len(array_trainx[0])

    for i in range(rowsNum):
        for j in range(rowLen):
            array_trainx[i][j] = float(array_trainx[i][j])
    XminCol = []
    XminCol.append(array_trainx[0].copy())
    for i in range(rowsNum):
        for j in range(rowLen):
            if array_trainx[i][j] < XminCol[0][j]:
                XminCol[0][j] = array_trainx[i][j]
    XmaxCol = []
    XmaxCol.append(array_trainx[0].copy())
    for i in range(rowsNum):
        for j in range(rowLen):
            if array_trainx[i][j] > XmaxCol[0][j]:
                XmaxCol[0][j] = array_trainx[i][j]

    for i in range(rowsNum):
        for j in range(rowLen):
            array_trainx[i][j] = (array_trainx[i][j] - XminCol[0][j]) / (XmaxCol[0][j] - XminCol[0][j])
    # noramilze test_x
    f = open(testExemple, "r")
    s = f.read().replace('W', '1')
    s = s.replace('R', '0')
    f.close();
    rowsNum = 0
    for line in s.splitlines():
        rowsNum += 1
        array_testx.append(line.split(","))
    rowLen = len(array_testx[0])
    for i in range(rowsNum):
        for j in range(rowLen):
            array_testx[i][j] = float(array_testx[i][j])
    for i in range(rowsNum):
        for j in range(rowLen):
            array_testx[i][j] = (array_testx[i][j] - XminCol[0][j]) / (XmaxCol[0][j] - XminCol[0][j])

    largestInex = []
    resultsKNN = []
    k = 7
    cntr=0
    for i in array_testx:
        dist_table = []
        for j in array_trainx:
            dist_table.append(distance.euclidean(i, j))
        largestInex.append(sorted(range(len(dist_table)), key=lambda sub: dist_table[sub])[:k])
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

    #preceptron
    learnRate=0.1
    iterNum=5
    classMatrix=[[0 for x in range(13)] for y in range(3)]
    copy_x=[]
    kmax=[]
    for i in array_trainx:
        copy_x.append(copy.deepcopy(i))
    for i in copy_x:
        i.append(1.0)
    for i in range(iterNum):
        for j in range(len(copy_x)):
            for k in range(len(classMatrix)):
                y=np.transpose(classMatrix[k])
                kmax.append(np.dot(y,copy_x[j]))
            kmax.index(max(kmax))
            if array_trainy[j]!=k:
                classMatrix[array_trainy[j]]+=(learnRate*copy_x[j])
                classMatrix[k]-=(learnRate*copy_x[j])

    copy_test_x=[]
    for i in array_testx:
        copy_test_x.append(copy.deepcopy(i))
    for i in copy_test_x:
        i.append(1.0)
    kmax=[]
    for i in range(iterNum):
        for j in range(len(copy_test_x)):
            for k in range(len(classMatrix)):
                y=np.transpose(classMatrix[k])
                kmax.append(np.dot(y,copy_test_x[j]))

    print("sfc")




if __name__ == '__main__':
    main()
