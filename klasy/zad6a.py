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
        car.numberofcars += 1
        car.listOfCars.append(self)

    def isdamaged(self):
        return not(self.isAirBagOK and self.isPaintingOK and self.isMechanicOK)

    def getinfo(self):
        print("{} {}".format(self.brand, self.model).upper())
        print("Air Bag   - ok -   {}".format(self.isAirBagOK))
        print("Painting  - ok -   {}".format(self.isPaintingOK))
        print("Mechanic  - ok -   {}".format(self.isMechanicOK))
        print("IS ON SALE          {}".format(self.__isOnSale))
        print('------------------------------------------')

    def __getisOnSale(self):
        return self.__isOnSale

    def __setisOnSale(self, newisOnSale):
        if self.brand == brandOnSale:
            self.__isOnSale = newisOnSale
            print("Changing status isOnSale to {} for {}".format(self.__isOnSale, self.brand))
        else:
            print("Cannot change status isOnSale. Sale valid only for {}".format(brandOnSale))

    isOnSale = property(__getisOnSale, __setisOnSale,None, 'id set to true the car is avaialable in sale/promo') # #służy do ukrywania atrybutów 



car01 = car("seat", "ibiza", True, True, True, False)
car02 = car("opel", "corsa", True, False, True, True)

# print("status of sale for {} is {}".format(car01.brand, car01.__getisOnSale()))
# car01.__setisOnSale(True)
# car02.__setisOnSale(False)
# print("status of sale for {} is {}".format(car02.brand, car02.__getisOnSale()))
car01.__setisOnSale(True)
car02.__setisOnSale(True)
print("status of sale for {} is {}".format(car02.isOnSale, car02.isOnSale()))

