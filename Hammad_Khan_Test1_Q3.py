class Cities:
    def __init__(self, city):
        self.city = city
        self.temp = []

    def enterTemp(self):
        for i in range (3):
            t = float(input("Enter in the temperature of %s on day %d: " % (self.city, i+1)))
            self.temp.append(t)

    def displayTemp(self):
        print(self.city, "recorded the following temperatures ", self.temp)

    def calcAvgTemp(self):
        summation = sum(self.temp)
        avg = summation/len(self.temp)
        print("The average temperature for ", self.city, " across these days was: %.1f" % float(avg))

city1 = Cities("New York")
city1.enterTemp()

city2 = Cities("Toronto")
city2.enterTemp()

city3 = Cities("Paris")
city3.enterTemp()

city1.displayTemp()
city2.displayTemp()
city3.displayTemp()

city1.calcAvgTemp()
city2.calcAvgTemp()
city3.calcAvgTemp()