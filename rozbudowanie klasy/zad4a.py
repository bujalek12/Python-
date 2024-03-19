#114 dziedziczenie klasy

brandOnSale = 'Opel'

class car(object):
    
    numberofcars = 0
    listOfCars = []

    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK,isOnSale,):
        print('>>>> this is __init__ of child class:', self.__class__.__name__))
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



class truck(car):
    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK,isOnSale, capacity):
        print('>> this is __init__ of child class:', self.__class__.__name__)
        super().__init__(brand, model, isAirBagOK, isPaintingOK, isMechanicOK,isOnSale)
        # moze byc z selfem i klassa super(truck,self).__init__(brand, model, isAirBagOK, isPaintingOK, isMechanicOK,isOnSale)
        #car.__init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK,isOnSale)
        self.capacity = capacity

    def getinfo(self):
        super().getinfo()
        print('capacity: {}'.format(self.capacity))


truck_01 = truck('Renault', 'Kangoo', True, True, True, False, 500)
truck_02 = truck('Renault', 'trafic', True, True, True, False, 1000)

print('calling properties:')
print(truck_01.brand, truck_01.model, truck_01.isOnSale, truck_01.capacity, truck_02.brand, truck_02.model, truck_02.isOnSale, truck_02.capacity)

truck_01.getinfo()
truck_02.getinfo()