#108
import random

class memoryclass:

    list_of_already_selected_items = []

    def __init__(self,funct):
        print('>> this is innit memoryclass')
        self.funct = funct

    def __call__(self, list):
        print('>> this is call memoryclass instance')
        items_not_selected = [i for i in list if i not in memoryclass.list_of_already_selected_items]
        print('>> items_not_selected:', items_not_selected)
        item = self.funct(items_not_selected)
        memoryclass.list_of_already_selected_items.append(item)
        return item

carsy = ['opel','toyota','Fiat','Fort','Mercedes', 'BMW', 'peguot','Porshe','VW', 'Mazda']

@memoryclass
def selecttodaypromotion(list_of_cars):
    return random.choice(list_of_cars)

@memoryclass
def selecttodayshow(list_of_cars):
    return random.choice(list_of_cars)

@memoryclass
def selecttodayaccesories(list_of_cars):
    return random.choice(list_of_cars)


print("promotion:", selecttodaypromotion(carsy))
print("show:", selecttodayshow(carsy))
print("accesories:", selecttodayaccesories(carsy))