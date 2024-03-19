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

    @classmethod   
    def ReadFromText(cls,aText):
        aNewCar = cls(*aText.split(':'))
        return aNewCar 

    @staticmethod 
    def convert_KM_KW(KM):
        return KM*0.7355 
    
    @staticmethod 
    def convert_KW_KM(KW):
        return KW*1.36



car01 = car("seat", "ibiza", True, True, True, False)
car02 = car("opel", "corsa", True, False, True, True)


lineodtext = 'Renault: Megane: True: True: False: False'
car03 = car.ReadFromText(lineodtext)

car03.getinfo()




print('converting 120km to KW',car.convert_KM_KW(120))
print('converting 90 Kw to KM',car.convert_KW_KM(90))

