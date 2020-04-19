import warnings
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import codecs
import math
from statistics import stdev
warnings.simplefilter(action='ignore', category=FutureWarning)

def makeAllInt(list1):
    list2 = []
    for x in list1:
        list2.append(int(x))
    return list2


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
            info = x.split('\t')
            self.year.append(info[0])
            self.causeName113.append(info[1])
            self.causeName.append(info[2])
            self.state.append(info[3])
            self.deaths.append(info[4])


    def deathFromCauses(self, givenCauseName):
        allDeaths = []
        for i in range(0, len(self.causeName)):
            if self.causeName[i] == givenCauseName and self.state[i] != "United States":
                allDeaths.append(self.deaths[i])
        return allDeaths

    def deathsFromOnlySuicide(self):
        suicideDeaths = []
        for i in range(0, len(self.causeName)):
            if self.causeName[i] == "Suicide" and self.state[i] != "United States":
                suicideDeaths.append(self.deaths[i])
        return suicideDeaths

    def createHistogram(self, list1, causeName):
        maxNum = self.getMaxNum(list1)
        binIntervals = self.createBinWithScottsRule(list1)
        listX =self.createBinSizesAndCreateY(maxNum, int(binIntervals),list1)
        list2 = makeAllInt(list1)
        plt.hist(list2,bins = listX)
        plt.title(causeName + " Death Rate Histogram Plot")
        plt.xlabel("Death Ranges of " + causeName)
        plt.ylabel("Number of death within ranges for every " + str(int(binIntervals)) + " interval")
        plt.show()

    def createLogPlot(self, list1, causeName):
        maxNum = self.getMaxNum(list1)
        binIntervals = self.createBinWithScottsRule(list1)
        listX = self.createBinSizesAndCreateY(maxNum, int(binIntervals),list1)
        listY = self.createY2(listX,list1)
        plt.scatter(listX, listY, c='g')
        plt.plot(listX, listY, c='g')
        plt.title(causeName + " Death Rate Histogram Log Log Plot")
        plt.xlabel("Death Ranges of " + causeName)
        plt.ylabel("Number of death within ranges for every " + str(int(binIntervals)) + " interval")
        plt.yscale('log')
        plt.xscale('log')


        plt.show()

# creating bin functions
    def createBinWithIQR(self,list1):
        Q1 = list1[len(list1)/4]
        Q3 = list1[((len(list1)/4) * 3)]
        IQR = int(Q1) - int(Q3)
        x = len(list1)
        ans = 2*(IQR/(len(list1)**(1/3)))  #freedman draconis
        return ans

    def createBinWithScottsRule(self, list1):
        intList = []
        for x in list1:
            intList.append(int(x))
        sd = stdev(intList)
        denom = (len(list1) ** .3333)
        ans = (sd*3.49)/denom
        return ans

    def createBinSizesAndCreateY(self, n, b,list1):
        counter = 1
        number = 0
        x = []
        x.append(0)

        while number <= int(n):
            number = number + b
            x.append(number)
            counter = counter + 1

        return x

    def createBinIntervalsWithSturgeRule(self, list1): # Sturge
        print(len(list1))
        binIntervals = 1 + (math.log(len(list1)) * 3.322)
        return binIntervals

    def createY2(self, listX, list1):
        ans = []
        for i in range(0, len(listX)):
            ans.append(0)

        for i in list1:
            for j in range(0, len(listX)):
                if int(i) < listX[j]:
                    ans[j] = ans[j] + 1
                    break
        return ans


    def createY(self, listX, list1):
        ans = []
        for i in range(0, 52):
            ans.append(0)

        for i in list1:
            for j in range(0, len(listX)):
                if int(i) < listX[j]:
                    ans[j] = ans[j] + 1
                    break
        return ans



    def createBinSize(self, num):
        listX = []
        binSize = int(num) / 50
        currentBin = 0
        for i in range(0, 52):
            listX.append(currentBin)
            currentBin = currentBin + binSize
        return listX

    def getMaxNum(self, list1):
        num = 0
        for i in range(0, len(list1)):
            if num < int(list1[i]):
                num = list1[i]
        return num

    def allCausesName(self):
        distinctNames = []
        for i in range(0, len(self.causeName)):
            if not distinctNames.__contains__(self.causeName[i]) and self.causeName[i] != 'Cause Name':
                distinctNames.append(self.causeName[i])
        return distinctNames

    def allYears(self):
        distinctYears = []
        for i in range(0, len(self.causeName)):
            if not distinctYears.__contains__(self.year[i]) and self.year[i] != 'Year':
                distinctYears.append(self.year[i])
        return distinctYears


def printHistogram():
    list1 = data.allCausesName()
    for i in range(0, len(list1)):
        data.createHistogram(data.deathFromCauses(list1[i]), list1[i])


def printLogPlot():
    list1 = data.allCausesName()
    for i in range(0, len(list1)):
        data.createLogPlot(data.deathFromCauses(list1[i]), list1[i])


def printHistogramAtIndex(num):
    list1 = data.allCausesName()
    data.createHistogram(data.deathFromCauses(list1[num]),list1[num])


def printLogPlotAtIndex(num):
    list1 = data.allCausesName()
    data.createLogPlot(data.deathFromCauses(list1[num]),list1[num])

def printHistAndLog(num):
    list1 = data.allCausesName()
    data.createHistogram(data.deathFromCauses(list1[num]), list1[num])
    data.createLogPlot(data.deathFromCauses(list1[num]), list1[num])

def printAllHistogram():
    list1 = data.allCausesName()
    for i in range(0, len(list1)):
        data.createHistogram(data.deathFromCauses(list1[i]), list1[i])

def printAllLog():
    list1 = data.allCausesName()
    for i in range(0, len(list1)):
        data.createLogPlot(data.deathFromCauses(list1[i]), list1[i])

def printAllGraphs():
    list1 = data.allCausesName()
    for i in range(0, len(list1)):
        data.createHistogram(data.deathFromCauses(list1[i]), list1[i])
        data.createLogPlot(data.deathFromCauses(list1[i]), list1[i])


def menu():
    i = 1
    print("These are the choices")
    for x in data.allCausesName():
        print(str(i) + " " + x)
        i = i + 1
    print("12 Show All Tables")
    print("13 Menu")
    print("14 Quit")

f = codecs.open("deathRatesUS.txt", "r", "utf-16")


def menu2():
    print("\t1 Show Histogram")
    print("\t2 Show Log Log Plot")
    print("\t3 Show Both")

data = myData(f)
#printHistogram()
#printLogPlot()

x = 15

menu()

while(True):
    x = unicode(input("Enter to pick list: "))
    if x.isnumeric() == True:
        x = int(x)
    else:
        x = 15

    if x == 12:
        menu2()
        i = input("\tEnter Value Here to show list: ")
        if i == 1:
            printAllHistogram()
        elif i == 2:
            printAllLog()
        elif i == 3:
            printAllGraphs()
    elif x == 13:
        menu()
    elif x == 14:
        break
    elif x >= 15 or x < 0:
        print("Please enter a valid number")
    else:
        menu2()
        i = input("\tEnter Value Here to show list: ")
        if i == 1:
            printHistogramAtIndex(x - 1)
        elif i == 2:
            printLogPlotAtIndex(x - 1)
        elif i == 3:
            printHistAndLog(x - 1)













