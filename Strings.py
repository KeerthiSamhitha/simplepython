class MAN:
    attr1 = "mammal"
    attr2 = "good"
    attr3 = "bad"
    def setHeight(self, val):
        self.height = val
    def setWeight(self, val):
        self.weight = val
    def getWeight(self):
        return self.weight


x = MAN()
y = MAN()

x.setHeight(5.4)
x.setWeight(65)

y.setHeight(5.8)
y.setWeight(45)

print("Height of x is {}".format(x.__class__.setHeight))




#print("SATYA is a {} boy".format(x.__class__.attr3))
#print("SAMHITHA is a {} girl".format(y.__class__.attr2))