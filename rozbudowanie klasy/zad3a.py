#111
from logging import exception
import types

class car:
    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK,accessories):
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK
        self.accessories = accessories

    def getinfo(self):
        print("{} {}".format(self.brand, self.model).upper())
        print("Air Bag   - ok -   {}".format(self.isAirBagOK))
        print("Painting  - ok -   {}".format(self.isPaintingOK))
        print("Mechanic  - ok -   {}".format(self.isMechanicOK))
        print("Accessories: {}".format(self.accessories))
        print('------------------------------------------')

    def __iadd__(self, other): # służy do dodawania
        if type(other) is list:
            accessories = self.accessories
            accessories.extend(other)
            return car(self.brand, self.model, self.isAirBagOK, self.isPaintingOK, self.isMechanicOK,accessories)
        elif type(other) is str:
            accessories = self.accessories
            accessories.append(other)
            return car(self.brand, self.model, self.isAirBagOK, self.isPaintingOK, self.isMechanicOK,accessories)
        else:
            raise Exception("Nie można dodać do obiektu typu {}".format(type(other)))

    def __add__(self, other):
        if type(other) is car:
            return [self, other]
        else:
            raise Exception("Nie można dodać do obiektu typu {}".format(type(other)))

    def __str__(self):
        return "Brand {} Model {}".format(self.brand, self.model).upper()
car_01=car("seat","ibiza",True,True,True,["cruise control","air conditioning"])
car_01.getinfo()
car_01 += 'parking assist'
car_01.getinfo()
car_02=car("opel","corsa",True,False,True,["cruise control","air conditioning"])
car_02.getinfo()
car_pack = car_01 + car_02
print('car_01 + car_02 = ', car_pack[0].brand,car_pack[1].brand)

print(car_01)
