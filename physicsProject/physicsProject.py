import matplotlib.pyplot as plt


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

    def getAllDeath(self):
        for x in self.deaths:
            print(x)


f = open("deathRatesUS.txt", "r")
data = myData(f)
data.getAllDeath()
