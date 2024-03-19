class car:

    def __init__(self, brand, model,isOnSale,):
        self.brand = brand
        self.model = model
        self.__isOnSale = isOnSale # atrybut prywatny blokuje dostęp z zewnątrz
        self.name = "{} {}".format(brand, model)


    def getinfo(self):
        print("{} {}".format(self.brand, self.model).upper())
        super().getinfo()
        print("IS ON SALE          {}".format(self.__isOnSale))
        print('------------------------------------------')


class specialist:
    def __init__(self,firstname,lastname,brand):
        self.firstname = firstname
        self.lastname = lastname
        self.name = "{} {}".format(firstname, lastname)
        self.brand = brand

    def getinfo(self):
        print('{} {} - ({})'.format(self.firstname, self.lastname, self.brand))



class carspecialist(car,specialist):
    def __init__(self, brand, model,isOnSale,firstname,lastname):
        print('>> this is __init__ of child class:', self.__class__.__name__)
        car.__init__(self, brand, model,isOnSale)
        specialist.__init__(self,firstname,lastname,brand)

    


tom = carspecialist('Renault', 'Kangoo', True, 'Tom', 'Smith')
print(vars(tom))