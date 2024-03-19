#własciwości klasy

brandOnSale = 'Opel'

class car:
    
    numberofcars = 0
    listOfCars = []

    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK,isOnSale,):
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK
        self.__isOnSale = isOnSale # atrybut prywatny blokuje dostęp z zewnątrz


    def isdamaged(self):
        return not(self.isAirBagOK and self.isPaintingOK and self.isMechanicOK)

    def getinfo(self):
        print("{} {}".format(self.brand, self.model).upper())
        print("Air Bag   - ok -   {}".format(self.isAirBagOK))
        print("Painting  - ok -   {}".format(self.isPaintingOK))
        print("Mechanic  - ok -   {}".format(self.isMechanicOK))
        print("IS ON SALE          {}".format(self.__isOnSale))
        print('------------------------------------------')

    @property
    def isOnSale(self):
        return self.__isOnSale

    @isOnSale.setter
    def isOnSale(self, newisOnSale):
        if self.brand == brandOnSale:
            self.__isOnSale = newisOnSale
            print("Changing status isOnSale to {} for {}".format(self.__isOnSale, self.brand))
        else:
            print("Cannot change status isOnSale. Sale valid only for {}".format(brandOnSale))
    
    @isOnSale.deleter
    def isOnSale(self):
        self.__isOnSale = None

    @property
    def CarTitle(self):
        return "{} {}".format(self.brand, self.model).title()

car01 = car("seat", "ibiza", True, True, True, False)
car02 = car("opel", "corsa", True, False, True, True)


print(car01.isOnSale)
car01.isOnSale = True

