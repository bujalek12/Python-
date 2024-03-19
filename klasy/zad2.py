class car:
    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK):
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK





car01 = car("seat", "ibiza", True, True, True)
car02 = car("opel", "corsa", True, False, True)

print(car01.brand, car01.model, car01.isAirBagOK, car01.isPaintingOK, car01.isMechanicOK)
print(car02.brand, car02.model, car02.isAirBagOK, car02.isPaintingOK, car02.isMechanicOK)



# car_01 = {
#     "brand": "seat",
#     "model": "ibiza",
#     "isAirBagOK": True,
#     "isPaintingOK": True,
#     "isMechanicOK": True,
# }

# car_02 = {
#     "brand": "opel",
#     "model": "corsa",
#     "isAirBagOK": True,
#     "isPaintingOK": False,
#     "isMechanicOK": True,
# }

# def iscardamaged(aCar):
#     return not (aCar["isAirBagOK"] and aCar["isPaintingOK"] and aCar["isMechanicOK"])

# print("is my car damage?", iscardamaged(car_01))

# print("is my car damage?", iscardamaged(car_02))

# cars = [car_01, car_02]

# for c in cars:
#     print("{} {} damaged? = {}".format(c["brand"], c["model"], iscardamaged(c)))