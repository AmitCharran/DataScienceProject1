
#
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



f = open("Data.txt", "r")

suicide = myData(f)
# print(suicide.deaths[10])

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


