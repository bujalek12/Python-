#dodawanie i ukrywanie atrybutów

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



car01 = car("seat", "ibiza", True, True, True, False)
car02 = car("opel", "corsa", True, False, True, True)

# car02.car__isOnSale = False # nie można zmienić wartości atrybutu prywatnego
# car02.YearOfProduction = 2010 # można dodawać nowe atrybuty
# del car02.YearOfProduction # można usuwać atrybuty

setattr(car02, 'Taxi', False) # można zmieniać wartość atrybutu
delattr(car02, 'Taxi') # można usuwać atrybuty
print(hasattr(car02, 'Taxi')) # sprawdza czy atrybut istnieje


car02.getinfo()
print(vars(car02)) # wypisuje wszystkie atrybuty obiektu

