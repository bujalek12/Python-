class memoryClass:
    def __init__(self, list):
        self.list_of_items = list

    def __call__(self,item):
        self.list_of_items.append(item)

mem = memoryClass([])
print("mem.list_of_items = ", mem.list_of_items)


#1
mem.list_of_items.append('buy sugar')
print("mem.list_of_items = ", mem.list_of_items)

print('this class is callable:', callable(memoryClass))
print('this class is callable:', callable(mem))

mem('buy milk')
mem('buy bread')
print("mem.list_of_items = ", mem.list_of_items)
