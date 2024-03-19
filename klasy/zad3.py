class car:
    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK):
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK

    def isdamaged(self):
        return not(self.isAirBagOK and self.isPaintingOK and self.isMechanicOK)

    def getinfo(self):
        print("{} {}".format(self.brand, self.model).upper())
        print("Air Bag   - ok -   {}".format(self.isAirBagOK))
        print("Painting  - ok -   {}".format(self.isPaintingOK))
        print("Mechanic  - ok -   {}".format(self.isMechanicOK))
        print('------------------------------------------')




car01 = car("seat", "ibiza", True, True, True)
car02 = car("opel", "corsa", True, False, True)

print(car01.brand, car01.model, car01.isdamaged())
print(car02.brand, car02.model, car02.isdamaged())

car01.getinfo()
car02.getinfo()

print(car01.brand, car01.model, car01.isAirBagOK, car01.isPaintingOK, car01.isMechanicOK)
print(car02.brand, car02.model, car02.isAirBagOK, car02.isPaintingOK, car02.isMechanicOK)
