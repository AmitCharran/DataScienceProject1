

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class myData:
    year = []
    causeName113 = []
    causeName = []
    state = []
    deaths = []

    def __init__(self, f):
        self.createData(f)

    def createData(self, f):
        for x in f:
            data = x.split('\t')
            self.year.append(data[0])
            self.causeName113.append(data[1])
            self.causeName.append(data[2])
            self.state.append(data[3])
            self.deaths.append(data[4])

    def getAllDeaths(self):
        for x in self.deaths:
            print(x)

    def getAllYears(self):
        for x in self.year:
            print(x)

    def getAllState(self):
        for x in self.state:
            print(x)

    def getAllCauseName(self):
        for x in self.causeName:
            print(x)

    def getAllCauseName113(self):
        for x in self.causeName113:
            print(x)

    def createPlot(self):
        deathNum = self.deaths
        del deathNum[0]
        maxNum = self.getMaxNum(deathNum)
        listX = self.createBinSizes(maxNum)
        listY = self.createListY()

        self.populateListY(listY, listX, deathNum)
        plt.bar(listX,listY)
        plt.show()


    def populateListY(self,listY, listX, deathNum):
        for i in deathNum:
            for j in range(0,len(listX)):
                if int(i) < listX[j]:
                    listY[j] = listY[j] + 1
                    break

    def createListY(self):
        ans = []
        for x in range(0,52):
            ans.append(0)
        return ans

    def createBinSizes(self, maxNum):
        binSize = int(maxNum)/50
        bin = []
        binNum = 0
        for x in range(0,52):
            bin.append(binNum)
            binNum = binNum + binSize
        return bin


    def getMaxNum(self, list):
        num = 0
        for x in list:
            if int(x) > int(num):
                num = x
        return num

f = open("Data.txt", "r")

suicide = myData(f)

suicide.createPlot()





