# CarBrand = "seat"
# CarModel = "ibiza"
# CarIsAirBagOK = True
# CarIsPaintingOK = True
# CarIsMechanicOK = True

car_01 = {
    "brand": "seat",
    "model": "ibiza",
    "isAirBagOK": True,
    "isPaintingOK": True,
    "isMechanicOK": True,
}

car_02 = {
    "brand": "opel",
    "model": "corsa",
    "isAirBagOK": True,
    "isPaintingOK": False,
    "isMechanicOK": True,
}

def iscardamaged(aCar):
    return not (aCar["isAirBagOK"] and aCar["isPaintingOK"] and aCar["isMechanicOK"])

print("is my car damage?", iscardamaged(car_01))

print("is my car damage?", iscardamaged(car_02))

cars = [car_01, car_02]

for c in cars:
    print("{} {} damaged? = {}".format(c["brand"], c["model"], iscardamaged(c)))