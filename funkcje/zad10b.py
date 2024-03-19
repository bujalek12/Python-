


text_list = ['x','xxx','xxxxx','xxxxxxx','']

#Przygotuj i zapisz w zmiennej f  funkcję lambda, która dla argumentu będącego napisem zwróci jego długość

f = lambda x: len(x)

#Przetestuj działanie funkcji na dowolnym napisie

print(f('Ala ma kota'))
#Uruchom funkcję f na każdym elemencie listy text_list. Wykorzystasz przy tym 
# funkcję map, 
# która pozwala uruchomić wskazywaną przez pierwszy argument funkcję dla 
# listy przekazanej jako drugi argument.


print(list(map(f, text_list)))

#Zmień wywołanie  funkcji map tak, żeby funkcja nie była zapisywana w 
# zmiennej f, ale 
# zamiast tego definiowana dynamicznie w wywołaniu funkcji map

print(list(map(lambda x : len(x), text_list)))