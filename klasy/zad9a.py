
import csv
import types

def exportToFile_static(path, header, data):
    with open(path, mode = 'w',) as f:
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        writer.writerows(data)
    print("Data saved to file: {}".format(path))

def exportToFile_Class(cls,path):
    with open(path, mode = 'w',) as f:
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['brand','model','isAirBagOK','isPaintingOK','isMechanicOK','isOnSale'])
        for car in cls.listOfCars:
            writer.writerow([car.brand, car.model, car.isAirBagOK, car.isPaintingOK, car.isMechanicOK, car.isOnSale])
    print("Data saved to file: {}".format(path))

def exportToFile_instance(self, path):
    with open(path, mode = 'w',) as f:
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['brand','model','isAirBagOK','isPaintingOK','isMechanicOK','isOnSale'])
        writer.writerow([self.brand, self.model, self.isAirBagOK, self.isPaintingOK, self.isMechanicOK, self.isOnSale])
    print("Data saved to file: {}".format(path))




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


print('static--------'*10)
car.ExportToFile_Static = exportToFile_static  # type: ignore
#exportToFile_static(r'C:\Users\48530\Desktop\visual\pythondlasredniozaaw\klasy\cars.csv', ['brand', 'model','isOnSale'], [[car.brand, car.model, car.isAirBagOK, car.isPaintingOK, car.isMechanicOK, car.isOnSale] for car in car.listOfCars])
car.ExportToFile_Static(r'C:\Users\48530\Desktop\visual\pythondlasredniozaaw\klasy\cars.csv', ['brand', 'model','isOnSale'], [[car.brand, car.model, car.isAirBagOK, car.isPaintingOK, car.isMechanicOK, car.isOnSale] for car in car.listOfCars])  # type: ignore
# print(dir(car))


print('Class--------'*10)
car.ExportToFile_Class = types.MethodType(exportToFile_Class, car)  # type: ignore
car.ExportToFile_Class(path = r'C:\Users\48530\Desktop\visual\pythondlasredniozaaw\klasy\cars2.csv')  # type: ignore

print('Instance--------'*10)
car01.ExportToFile_Instance = types.MethodType(exportToFile_instance,car01)
car01.ExportToFile_Instance(path = r'C:\Users\48530\Desktop\visual\pythondlasredniozaaw\klasy\cars3.csv')


print('-'*50)
if hasattr(car01, 'ExportToFile_Static') and callable(car01.ExportToFile_Static):
    print('car01 has ExportToFile_Static')
if hasattr(car01, 'ExportToFile_Class') and callable(car01.ExportToFile_Class):
    print('car01 has ExportToFile_Class')
if hasattr(car01, 'ExportToFile_Instance') and callable(car01.ExportToFile_Instance):
    print('car01 has ExportToFile_Instance')
if hasattr(car, 'ExportToFile_Staticxx') and callable(car.ExportToFile_Static):
    print('car has ExportToFile_Static')
else:
    print('car has not ExportToFile_Staticxxx')

