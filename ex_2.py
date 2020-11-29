import numpy as np
import scipy
import sys

def main():
    trainExemple=sys.argv[1]
    trainLabels=sys.argv[2]
    testExemple=sys.argv[3]
    f=open(trainExemple,"r")
    s = f.read().replace('W','1')
    s=s.replace('R','0')
    # s = s.replace('\n', '')
    f.close();
    f=open(trainExemple,"w")
    f.write(s)
    f.close();
    f = open(trainExemple, "r")
    array=[]
    rowsNum=0
    for line in f:
        rowsNum+=1
        array.append(line.split(","))
    f.close()
    rowLen=len(array[0])

    for i in range(rowsNum):
        for j in range(rowLen):
            if(array[i][j]=="1\n"):
                array[i][j]="1"
            if(array[i][j]=="0\n"):
                array[i][j]="0"
            array[i][j]=float(array[i][j])
    XminCol=[]
    XminCol.append(array[0].copy())
    for i in range(rowsNum):
        for j in range(rowLen):
            if array[i][j]<XminCol[0][j]:
                XminCol[0][j] =array[i][j]

    XmaxCol = []
    XmaxCol.append(array[0].copy())
    for i in range(rowsNum):
        for j in range(rowLen):
            if array[i][j] > XmaxCol[0][j]:
                XmaxCol[0][j] = array[i][j]

    for i in range(rowsNum):
        for j in range(rowLen):
            array[i][j]=(array[i][j]-XminCol[0][j])/(XmaxCol[0][j] -XminCol[0][j])
    print("sfc")

if __name__ == '__main__':
    main()
